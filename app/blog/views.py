from flask import Blueprint, render_template, abort
from app.core.db import db
from app.core.models import *
blog_views = Blueprint('blog', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@blog_views.route('/blog')
def blog():
    blog = Blog.query.all()
    nopost = None
    if not blog:
        nopost = 'No Post'
    return render_template('blog.html', **locals())


@blog_views.route('/blog/<id>/')
def show_post(id):
	blog = Blog.query.filter_by(id=id).first_or_404()
	return render_template('post.html', blog=blog)

@blog_views.route('/blog/category/')
def blog_category():
	category = db.session.query(Category).all()
	return render_template('category.html', **locals())


@blog_views.route('/blog/category/<category_id>/')
def show_category(category_id):
	blog = Blog.query.filter(Blog.category_id.endswith(category_id)).all()
	return render_template('category_post.html', **locals())
