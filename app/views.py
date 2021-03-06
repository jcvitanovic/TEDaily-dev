from flask import render_template,g
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from oauth import OAuthSignIn
from models import User
from flask import Flask, redirect, url_for, render_template
from forms import LoginForm, EditForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user = g.user
    return render_template('index.html',
                           title='Home',
                           user=user)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login')
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))    
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))    


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    return render_template('user.html',
                           user=user)    

@app.before_request
def before_request():
	g.user = current_user 

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))    

@app.route('/edit', methods=['GET','POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    return render_template('edit.html', form = form)