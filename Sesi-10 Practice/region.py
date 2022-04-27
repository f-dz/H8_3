from flask import make_response, abort
from config import db
from models import Region, RegionSchema


def read_all():
    # Create the list of region from our data
    list_region = Region.query.order_by(Region.regionid).all()

    # Serialize the data for the response
    region_schema = RegionSchema(many=True)
    data = region_schema.dump(list_region)
    return data


def read_one(regionid):
    # Get the region requested
    region = Region.query.filter(Region.regionid == regionid).one_or_none()

    if region is not None:
        # Serialize the data for the response
        region_schema = RegionSchema()
        data = region_schema.dump(region)
        return data
    else:
        abort(
            404,
            "Region data not found for Id: {regionid}".format(regionid=regionid),
        )


def create(region):
    region_content = region.get('region')

    existing_data = Region.query.filter(Region.region == region_content).one_or_none()

    if existing_data is None:
        schema = RegionSchema()
        new_data = schema.load(region, session=db.session)
        # Add region data to the database
        db.session.add(new_data)
        db.session.commit()
        # Serialize and return the newly created region data in the response
        data = schema.dump(new_data)
        return data, 201
    else:
        abort(409, f"Region data '{region_content}' already exists")


def update(regionid, region):
    region_content = region.get('region')

    existing_data = Region.query.filter(Region.region == region_content).one_or_none()

    # Get region data requested from the db into session
    update_region = Region.query.filter(Region.regionid == regionid).one_or_none()

    if existing_data is None:
        if update_region is not None:
            # turn the passed in region data into a db object
            schema = RegionSchema()
            update = schema.load(region, session=db.session)
            # Set the id's to region data we want to update
            update.regionid = update_region.regionid
            # merge the new object into the old and commit it to the db
            db.session.merge(update)
            db.session.commit()
            # return updated region data in the response
            data = schema.dump(update_region)
            return data, 200
        else:
            abort(404, f"region data not found for Id: {regionid}")
    else:
        abort(409, f"Region data '{region_content}' already exists")

def delete(regionid):
    # Get region data requested
    region = Region.query.filter(Region.regionid == regionid).one_or_none()

    if region is not None:
        db.session.delete(region)
        db.session.commit()
        return make_response(
            "Region data {regionid} deleted".format(regionid=regionid), 200
        )
    else:
        abort(
            404,
            "Region data not found for Id: {regionid}".format(regionid=regionid),
        )