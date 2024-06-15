from testapp import db
from datetime import datetime

class menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255))
    price = db.Column(db.String(255))
    number_of_count = db.Column(db.Integer)
    explanation = db.Column(db.String(255))
    product_image = db.Column(db.String(255))
