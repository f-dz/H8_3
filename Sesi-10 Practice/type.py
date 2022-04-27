from flask import make_response, abort
from config import db
from models import Type, TypeSchema


def read_all():
    # Create the list of type from our data
    list_type = Type.query.order_by(Type.typeid).all()

    # Serialize the data for the response
    type_schema = TypeSchema(many=True)
    data = type_schema.dump(list_type)
    return data


def read_one(typeid):
    # Get the type requested
    type = Type.query.filter(Type.typeid == typeid).one_or_none()

    if type is not None:
        # Serialize the data for the response
        type_schema = TypeSchema()
        data = type_schema.dump(type)
        return data
    else:
        abort(
            404,
            "Type data not found for Id: {typeid}".format(typeid=typeid),
        )


def create(type):
    type_content = type.get('type')

    existing_data = Type.query.filter(Type.type == type_content).one_or_none()

    if existing_data is None:
        schema = TypeSchema()
        new_data = schema.load(type, session=db.session)
        # Add type data to the database
        db.session.add(new_data)
        db.session.commit()
        # Serialize and return the newly created type data in the response
        data = schema.dump(new_data)
        return data, 201
    else:
        abort(409, f"Type data '{type_content}' already exists")

def update(typeid, type):
    type_content = type.get('type')

    existing_data = Type.query.filter(Type.type == type_content).one_or_none()
    
    # Get type data requested from the db into session
    update_type = Type.query.filter(Type.typeid == typeid).one_or_none()

    if existing_data is None:
        if update_type is not None:
            # turn the passed in type data into a db object
            schema = TypeSchema()
            update = schema.load(type, session=db.session)
            # Set the id's to type data we want to update
            update.typeid = update_type.typeid
            # merge the new object into the old and commit it to the db
            db.session.merge(update)
            db.session.commit()
            # return updated type data in the response
            data = schema.dump(update_type)
            return data, 200
        else:
            abort(404, f"type data not found for Id: {typeid}")
    else:
       abort(409, f"Type data '{type_content}' already exists")


def delete(typeid):
    # Get type data requested
    type = Type.query.filter(Type.typeid == typeid).one_or_none()

    if type is not None:
        db.session.delete(type)
        db.session.commit()
        return make_response(
            "Type data {typeid} deleted".format(typeid=typeid), 200
        )
    else:
        abort(
            404,
            "Type data not found for Id: {typeid}".format(typeid=typeid),
        )