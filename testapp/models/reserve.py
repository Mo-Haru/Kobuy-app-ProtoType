from testapp import db
from datetime import datetime

class reserve(db.Model):
    __tablename__ = 'reserve'
    id = db.Column(db.Integer, primary_key=True)
    reserver = db.Column(db.String(255))
    e_mail = db.Column(db.String(255))
    resreve_dic = db.Column(db.DateTime)
    reserve_time = db.Column(db.DateTime, default = datetime.now)
    cancel = db.Column(db.Boolean)