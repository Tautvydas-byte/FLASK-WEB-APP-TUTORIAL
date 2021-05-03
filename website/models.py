from . import db  # import fromt the current package
from flask_login import UserMixin  # without it would need everything from scratch
from sqlalchemy.sql import func

# One To Many


class Note(db.Model):
    # automaticaly increment by database
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # SQLAlchemy automaticaly added date
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'))  # always store id of User. from Class User take id. User become user, cause class must be from Capital letter,
    # but SQL  understand reference


class User(db.Model, UserMixin):  # creat DB tables
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # store all different lists. Relationship must be with Capital, but not for foreign key
    notes = db.relationship('Note')
