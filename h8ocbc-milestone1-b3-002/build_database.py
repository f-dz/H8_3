import os
from config import db
from models import Movie, Director
import json

# Delete database file if it exists currently
if os.path.exists('final_proj.db'):
    os.remove('final_proj.db')

# Create the database
db.create_all()

f = open('./assets/directors.json', encoding='utf-8')
DIRECTOR = json.load(f)
f.close()

f = open('./assets/movies.json', encoding='utf-8')
MOVIE = json.load(f)
f.close()

# Iterate over the DIRECTOR structure and populate the database
for item in DIRECTOR['directors']:
    data = Director(
        id = item["id"],
        name = item["name"],
        gender = item["gender"],
        uid = item["uid"],
        department = item["department"]
    )
    db.session.add(data)
db.session.commit()

# Iterate over the MOVIE structure and populate the database
for item in MOVIE['movies']:
    data = Movie(
        id = item["id"],
        original_title = item["original_title"],
        budget = item["budget"],
        popularity = item["popularity"],
        release_date = item["release_date"],
        revenue = item["revenue"],
        title = item["title"],
        vote_average = item["vote_average"],
        vote_count = item["vote_count"],
        overview = item["overview"],
        tagline = item["tagline"],
        uid = item["uid"],
        director_id = item["director_id"]
    )
    db.session.add(data)
db.session.commit()