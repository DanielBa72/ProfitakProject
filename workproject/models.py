from workproject import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date_of_birth = db.Column(db.String, nullable=False)
    comments = relationship('Comment', backref="user", lazy=True)

    def __init__(self, id, name, date_of_birth):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth


class Comment(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))

    def __init__(self, id, content, user_id):
        self.id = id 
        self.content = content
        self.user_id = user_id


