from flask import Blueprint, render_template, flash, redirect, url_for
from app.core.db import db
from app.core.models import Blog, Category
from .forms import CreatePostForm

admin_views = Blueprint('admin', __name__,
                        template_folder='../../templates/admin',
                        static_folder='../../static')

@admin_views.route('/admin/create_post', methods=['GET', 'POST'])
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
    	if form.validate():
	    	category = Category.query.filter_by(name_category = form.category.data).first()
	    	if category:
	    		form.category.data = category.id
	    	else:
	    		new_category = Category(form.category.data)
	    		db.session.add(new_category)
		    	db.session.commit()
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

@admin_views.route('/admin/success_create')
def success_create():
	return render_template('create_post_success.html')