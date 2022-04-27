from flask import make_response, abort
from config import db
from models import Director, DirectorSchema, Movie
from movie import read_one as movie_read_one


def read_all():
    # Create the list of director from our data
    list_director = Director.query.order_by(Director.id).limit(10).all()

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(list_director)
    return data


def read_one(id):
    # Get the director requested
    director = Director.query.filter(Director.id == id).one_or_none()

    if director is not None:
        # Serialize the data for the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data
    else:
        abort(
            404,
            f"Director data not found for Id: {id}",
        )


def read_director_profile(movie_id):
    # Create the list of movie from our data
    movie = movie_read_one(movie_id)

    director = read_one(movie["director_id"])
    return director


def create(director):
    id = director.get("id")
    uid = director.get("uid")

    existing_id = Director.query.filter(Director.id == id).one_or_none()

    existing_uid = Director.query.filter(Director.uid == uid).one_or_none()

    if existing_id is None:
        if existing_uid is None:
            schema = DirectorSchema()
            new_data = schema.load(director, session=db.session)
            # Add director data to the database
            db.session.add(new_data)
            db.session.commit()
            # Serialize and return the newly created director data in the response
            data = schema.dump(new_data)
            return data, 201
        else:
            abort(409, f"Director uid: {uid} already exists")
    else:
        abort(409, f"Director id: {id} already exists")


def update(id, director):
    uid = director.get("uid")

    # Get director data requested from the db into session
    update_director = Director.query.filter(Director.id == id).one_or_none()
    
    existing_data = Director.query.filter(Director.uid == uid).all()

    same_uid = (
        Director.query.filter(Director.id == id)
        .filter(Director.uid == uid)
        .one_or_none()
    )

    if ((same_uid is not None and len(existing_data) == 1) or
        (same_uid is None and len(existing_data) < 1)):
        if update_director is not None:
            # turn the passed in director data into a db object
            schema = DirectorSchema()
            update = schema.load(director, session=db.session)
            # Set the id's to director data we want to update
            update.id = update_director.id
            # merge the new object into the old and commit it to the db
            db.session.merge(update)
            db.session.commit()
            # return updated director data in the response
            data = schema.dump(update_director)
            return data, 200
        else:
            abort(404, f"Director data not found for Id: {id}")
    else:
        abort(409, f"Director uid: '{uid}' already exists")


def delete(id):
    # Get director data requested
    director = Director.query.filter(Director.id == id).one_or_none()
    # movie = movie_read(id)
    delete = Movie.__table__.delete().where(Movie.director_id == id)

    if director is not None:
        db.session.delete(director)
        db.session.execute(delete)
        db.session.commit()
        return make_response(
            f"Director id: '{id}' deleted", 200
        )
    else:
        abort(
            404,
            f"Director data not found for Id: {id}",
        )