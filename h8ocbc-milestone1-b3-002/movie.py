from flask import make_response, abort
from config import db
from models import Movie, MovieSchema, Director


def read_all():
    # Create the list of movie from our data
    list_movie = Movie.query.order_by(Movie.id).limit(10).all()

    # Serialize the data for the response
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(list_movie)
    return data


def read_one(id):
    # Get the movie requested
    movie = Movie.query.filter(Movie.id == id).one_or_none()

    if movie is not None:
        # Serialize the data for the response
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data
    else:
        abort(
            404,
            f"Movie data not found for Id: {id}",
        )


def read_movie_by_director(director_id):
    # Create the list of movie from our data
    list_movie = (
        Movie.query.filter(Movie.director_id == director_id)
        .order_by(Movie.id).all()
    )

    if len(list_movie) > 0:
        # Serialize the data for the response
        movie_schema = MovieSchema(many=True)
        data = movie_schema.dump(list_movie)
        return data
    else:
        abort(
            404,
            f"No movies directed by director Id: {director_id}",
        )


def read_top_three(column):
    data = []
    if column =='budget':
        list_movie = (
            Movie.query.order_by(db.desc(Movie.budget))
            .with_entities(Movie.title, Movie.budget).limit(3).all()
        )
        for row in list_movie:
            data.append(list(row))
        return data
    elif column == 'popularity':
        list_movie = (
            Movie.query.order_by(db.desc(Movie.popularity))
            .with_entities(Movie.title, Movie.popularity).limit(3).all()
        )
        for row in list_movie:
            data.append(list(row))
        return data
    elif column == 'revenue':
        list_movie = (
            Movie.query.order_by(db.desc(Movie.revenue))
            .with_entities(Movie.title, Movie.revenue).limit(3).all()
        )
        for row in list_movie:
            data.append(list(row))
        return data
    elif column == 'vote_average':
        list_movie = (
            Movie.query.order_by(db.desc(Movie.vote_average))
            .with_entities(Movie.title, Movie.vote_average).limit(3).all()
        )
        for row in list_movie:
            data.append(list(row))
        return data
    elif column == 'vote_count':
        list_movie = (
            Movie.query.order_by(db.desc(Movie.vote_count))
            .with_entities(Movie.title, Movie.vote_count).limit(3).all()
        )
        for row in list_movie:
            data.append(list(row))
        return data


def create(movie):
    id_movie = movie.get("id")
    uid = movie.get("uid")
    dir = movie.get("director_id")

    existing_dir = Director.query.filter(Director.id == dir).one_or_none()

    existing_id = Movie.query.filter(Movie.id == id_movie).one_or_none()

    existing_uid = Movie.query.filter(Movie.uid == uid).one_or_none()

    if existing_dir is not None:
        if existing_id is None:
            if existing_uid is None:
                schema = MovieSchema()
                new_data = schema.load(movie, session=db.session)
                # Add movie data to the database
                db.session.add(new_data)
                db.session.commit()
                # Serialize and return the newly created movie data in the response
                data = schema.dump(new_data)
                return data, 201
            else:
                abort(409, f"Movie with uid: {uid} already exists")
        else:
            abort(409, f"Movie with id: {id_movie} already exists")
    else:
        abort(404, f"Director data not found for Id: {dir}")


def update(id, movie):
    uid = movie.get("uid")
    dir = movie.get("director_id")
    
    # Get movie data requested from the db into session
    update_movie = Movie.query.filter(Movie.id == id).one_or_none()

    existing_dir = Director.query.filter(Director.id == dir).one_or_none()

    existing_data = (Movie.query.filter(Movie.uid == uid).all())

    same_uid = (
        Movie.query.filter(Movie.id == id)
        .filter(Movie.uid == uid)
        .one_or_none()
    )

    if existing_dir is not None:
        if ((same_uid is not None and len(existing_data) == 1) or
            (same_uid is None and len(existing_data) < 1)):
            if update_movie is not None:
                # turn the passed in movie data into a db object
                schema = MovieSchema()
                update = schema.load(movie, session=db.session)
                # Set the id's to movie data we want to update
                update.id = update_movie.id
                # merge the new object into the old and commit it to the db
                db.session.merge(update)
                db.session.commit()
                # return updated movie data in the response
                data = schema.dump(update_movie)
                return data, 200
            else:
                abort(404, f"Movie data not found for Id: {id}")
        else:
            abort(409, f"Movie with uid: {uid} already exists in another data")
    else:
        abort(404, f"Director data not found for Id: {dir}")


def delete(id):
    # Get movie data requested
    movie = Movie.query.filter(Movie.id == id).one_or_none()

    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            f"Movie data {id} deleted", 200
        )
    else:
        abort(
            404,
            f"Movie data not found for Id: {id}",
        )