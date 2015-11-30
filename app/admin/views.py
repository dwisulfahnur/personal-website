from flask import Blueprint, render_template, flash, redirect, url_for
from app.core.db import db
from app.core.models import Blog, Category
from .models import User
from .forms import CreatePostForm, LoginForm, UpdatePostForm
from werkzeug.security import check_password_hash
from flask.ext.login import current_user, login_user, logout_user, login_required

admin_views = Blueprint('admin', __name__,
                        template_folder='../templates/admin',
                        static_folder='../static')

##################################################  
###################Login&Logout###################
##################################################

@admin_views.route('/admin/', methods = ['GET','POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('.admin_home'))
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('.admin_home'))
            error = 'Invalid Password.'
        error = 'Unknown Username.'
    return render_template('login.html', form=form, error=error)

@admin_views.route('/logout/')
@login_required
def admin_logout():
    logout_user()
    flash('You\'re logger Out')
    return redirect(url_for('.admin_login'))

##################################################
###############End of Login&Logout################
##################################################

##################################################
####################Admin Home####################
##################################################

@admin_views.route('/admin/home/')
@login_required
def admin_home():
    user = current_user
    return render_template('home.html',user=user)

@admin_views.route('/admin/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        if form.validate():
            category = Category.query.filter_by(name_category = form.category.data).first()
            if category:
                form.category.data = category.id
            else:
                category_create(form.category.data)
                category = Category.query.filter_by(name_category = form.category.data).first()
                form.category.data = category.id
            post = Blog(form.title.data,
                        form.author.data,
                        form.content.data,
                        form.category.data)
            db.session.add(post)
            db.session.commit()
            flash('Your Post are posted.')
            return redirect(url_for('.success_create'))
    return render_template('create_post.html', form=form)

@admin_views.route('/admin/success_create/')
@login_required
def success_create():
	return render_template('create_post_success.html')

@admin_views.route('/admin/update_post/')
@login_required
def update_post():
    blog = Blog.query.all()
    nopost = None
    if not blog:
        nopost = 'No Post'
    return render_template('update_post.html', blog=blog, nopost=nopost)

@admin_views.route('/admin/delete_post/<id_post>')
@login_required
def delete_post(id_post):
    post = Blog.query.filter_by(id = id_post).first()
    flash('{} have been deleted'.format(post.title))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('.update_post'))


#function for create category to Database
def category_create(name_category):
    new_category = Category(name_category)
    db.session.add(new_category)
    db.session.commit()

@admin_views.route('/admin/edit_post/<id_post>', methods=['GET','POST'])
@login_required
def edit_post(id_post):
    form = UpdatePostForm()
    post = Blog.query.filter_by(id = id_post).first()
    if form.validate_on_submit():
        category = Category.query.filter_by(name_category = form.category.data).first()
        if category:
            form.category.data = category.id
        else:
            category_create(form.category.data)
            category = Category.query.filter_by(name_category = form.category.data).first()
            form.category.data = category.id
        post.title = form.title.data
        post.author = form.author.data
        post.content = form.content.data
        post.category_id = form.category.data
        db.session.commit()
        flash('Your Post are Update.')
        return redirect(url_for('.success_update'))
    return render_template('edit_post.html', form=form,post=post)

@admin_views.route('/admin/success_update/')
@login_required
def success_update():
	return render_template('update_post_success.html')

##################################################
#################End of Admin Home################
##################################################
