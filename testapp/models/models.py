from testapp import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    cls = db.Column(db.Integer, nullable=False)
    num = db.Column(db.Integer, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'


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

class Reserved(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255))
    product_image = db.Column(db.String(255))
    price = db.Column(db.String(255))