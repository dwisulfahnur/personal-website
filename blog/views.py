from flask import Blueprint, render_template
from flask.views import View
from db import db
from models import *
blog_views = Blueprint('blog', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@blog_views.route('/blog')
def blog():
	blog = db.session.query(Blog).all()
	personal_information = PersonalInformation.query.filter_by(id=2).first()
	return render_template('blog.html', **locals())


@blog_views.route('/blog/<id>')
def show_post(id):
	personal_information = PersonalInformation.query.filter_by(id=2).first()
	blog = Blog.query.filter_by(id=id).first_or_404()
	context = { 'personal_information' : personal_information,
				'blog' : blog
				}
	return render_template('post.html', **context)