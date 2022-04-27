from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema, Type, Region


def read_all():
    # Create the list of avocado from our data
    list_avocado = Avocado.query.order_by(Avocado.date).all()

    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(list_avocado)
    return data


def read_one(avocadoid):
    # Get the avocado requested
    avocado = Avocado.query.filter(Avocado.avocadoid == avocadoid).one_or_none()

    if avocado is not None:
        # Serialize the data for the response
        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(avocado)
        return data
    else:
        abort(
            404,
            "Avocado data not found for Id: {avocadoid}".format(avocadoid=avocadoid),
        )


def create(avocado):
    typeid = avocado.get('type')
    regionid = avocado.get('regionid')

    existing_type = Type.query.filter(Type.typeid == typeid).one_or_none()

    existing_region = Region.query.filter(Region.regionid == regionid).one_or_none()

    existing_data = (
        Avocado.query.filter(Avocado.type == typeid)
        .filter(Avocado.regionid == regionid)
        .one_or_none()
    )

    if existing_type is not None:
        if existing_region is not None:
            if existing_data is None:
                schema = AvocadoSchema()
                new_data = schema.load(avocado, session=db.session)
                # Add avocado data to the database
                db.session.add(new_data)
                db.session.commit()
                # Serialize and return the newly created avocado data in the response
                data = schema.dump(new_data)
                return data, 201
            else:
                abort(409, f"Avocado with type : {typeid} and region : {regionid} already exists")
        else:
            abort(404, f"Region data not found for Id: {regionid}")
    else:
        abort(404, f"Type data not found for Id: {typeid}")


def update(avocadoid, avocado):
    typeid = avocado.get('type')
    regionid = avocado.get('regionid')

    # Get avocado data requested from the db into session
    update_avocado = Avocado.query.filter(Avocado.avocadoid == avocadoid).one_or_none()

    existing_type = Type.query.filter(Type.typeid == typeid).one_or_none()

    existing_region = Region.query.filter(Region.regionid == regionid).one_or_none()

    existing_data = (
        Avocado.query.filter(Avocado.type == typeid)
        .filter(Avocado.regionid == regionid)
        .all()
    )

    same_type_region = (
        Avocado.query.filter(Avocado.avocadoid == avocadoid)
        .filter(Avocado.type == typeid)
        .filter(Avocado.regionid == regionid)
        .one_or_none()
    )

    if existing_type is not None:
        if existing_region is not None:
            if ((same_type_region is not None and len(existing_data) == 1) or
                (same_type_region is None and len(existing_data) < 1)):
                if update_avocado is not None:
                    # turn the passed in avocado data into a db object
                    schema = AvocadoSchema()
                    update = schema.load(avocado, session=db.session)
                    # Set the id's to avocado data we want to update
                    update.avocadoid = update_avocado.avocadoid
                    # merge the new object into the old and commit it to the db
                    db.session.merge(update)
                    db.session.commit()
                    # return updated avocado data in the response
                    data = schema.dump(update_avocado)
                    return data, 200
                else:
                    abort(404, f"Avocado data not found for Id: {avocadoid}")
            else:
                abort(409, f"Avocado with type : {typeid} and region : {regionid} already exists in another data")
        else:
            abort(404, f"Region data not found for Id: {regionid}")
    else:
        abort(404, f"Type data not found for Id: {typeid}")


def delete(avocadoid):
    # Get avocado data requested
    avocado = Avocado.query.filter(Avocado.avocadoid == avocadoid).one_or_none()

    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(
            "Avocado data {avocadoid} deleted".format(avocadoid=avocadoid), 200
        )
    else:
        abort(
            404,
            "Avocado data not found for Id: {avocadoid}".format(avocadoid=avocadoid),
        )