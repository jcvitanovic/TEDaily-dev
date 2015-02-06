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

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3

	def __repr__(self):
		return '<User %r>' % (self.nickname) 

class Preference:
	id = db.Column(db.Integer, primary_key = True)
	tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	

class Tag:
	id = db.Column(db.Integer, primary_key = True)
	tag_name = db.Column(db.String(64), nullable = False)



