import os
from config import db
from models import Type, Region, Avocado

# Delete database file if it exists currently
if os.path.exists('avocado.db'):
    os.remove('avocado.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
TYPE = [
    { 'type': 'conventional' },
    { 'type': 'organic' }
]
REGION = [
    { 'region': 'California' },
    { 'region': 'Bangkok' }
]
AVOCADO = [
    {
        'avgprice': 1.22,
        'totalvol': 40873.28,
        'avo_a': 2819.5,
        'avo_b': 28287.42,
        'avo_c': 49.9,
        'type': 1,
        'regionid': 1
    }
]

# Iterate over the TYPE structure and populate the database
for item in TYPE:
    data = Type(type=item.get("type"))
    db.session.add(data)
db.session.commit()

# Iterate over the REGION structure and populate the database
for item in REGION:
    data = Region(region=item.get("region"))
    db.session.add(data)
db.session.commit()

# Iterate over the AVOCADO structure and populate the database
for item in AVOCADO:
    data = Avocado(
        avgprice = item.get("avgprice"),
        totalvol = item.get("totalvol"),
        avo_a = item.get("avo_a"),
        avo_b = item.get("avo_b"),
        avo_c = item.get("avo_c"),
        type = item.get("type"),
        regionid = item.get("regionid")
    )
    db.session.add(data)
db.session.commit()
