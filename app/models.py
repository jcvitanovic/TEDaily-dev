from app import db
from hashlib import md5
from app import app
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user,\
    current_user

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)