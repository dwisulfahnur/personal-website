from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from forms import LoginForm
from models import User
from werkzeug.security import check_password_hash
from functools import wraps
from flask.ext.login import login_user, login_required, logout_user, current_user
from loginmanager import login_manager

user_views = Blueprint('user_views', __name__, template_folder='../../templates',
                                         static_folder='../../static'
                                         )


'''def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            flash('You need To login first.')
            return redirect(url_for('.login'))
    return wrap'''

@user_views.route('/home/')
@login_required
def home():
    user = User.query.filter_by(id = session['user_id']).first()
    return render_template('home.html', user=user)

@user_views.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    
    if form.validate_on_submit():
        if form.validate() is True:
            login_user(form.user)
            flash('you\'re logged in')
            return redirect(url_for('.home'))
    return render_template('login.html', form=form)

@user_views.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You\'re Logged out')
    return redirect(url_for('.login'))
