from flask import Flask
from flask import Flask, redirect, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user,\
    current_user
from oauth import OAuthSignIn

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config')
lm = LoginManager(app)
lm.login_view = 'login'
from app import views, models
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '1569948849912184',
        'secret': '9ff9afaacead3c1e3c54fa16e150bcb0'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    },
    'google' : {
        'id' : '390417106514-s4ko201tr5ueqnogq7ca8cium1cck2s3.apps.googleusercontent.com',
        'secret' : 'pJmsoWejR9aW_u40dVwHvw61'

    }
}



