from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.models import User


class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
	nickname = StringField('nickname', validators = [DataRequired()])
	about_me = TextAreaField('about_me', validators = [DataRequired()])
	
	def __init__(self, original_nickname, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		#self.original_nickname = original_nickname