from datetime import datetime
from app.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=datetime.now)
