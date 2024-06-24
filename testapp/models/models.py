from testapp import db
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255))
    price = db.Column(db.String(255))
    number_of_count = db.Column(db.Integer)
    explanation = db.Column(db.String(255))
    product_image = db.Column(db.String(255))

class Reserve(db.Model):
    __tablename__ = 'reserve'
    id = db.Column(db.Integer, primary_key=True)
    reserver = db.Column(db.String(255))
    e_mail = db.Column(db.String(255))
    resreve_dic = db.Column(db.String(255))
    reserve_time = db.Column(db.DateTime, default = datetime.now)
    cancel = db.Column(db.Boolean)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now)