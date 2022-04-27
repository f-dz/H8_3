from xml.etree.ElementInclude import include
from config import db, ma
from datetime import datetime, timedelta

class Type(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)

class Region(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.Text)

class Avocado(db.Model):
    __tablename__ = 'avocado'
    avocadoid = db.Column(db.Integer, primary_key=True)
    date = db.Column(
        db.Text, default=datetime.now().strftime(("%Y-%m-%d"))
    )
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))

class TypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Type
        load_instance = True 

class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region
        load_instance = True 

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        load_instance = True 
        include_fk = True