from flask import Blueprint, render_template
from db import db
from models import *

admin_views = Blueprint('admin', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@admin_views.route('/admin/')
def activities():
	posts = None
	personal_information = PersonalInformation.query.filter_by(id=2).first()
	context = {	'posts' : posts,
				'personal_information' : personal_information
			  }
	return render_template('admin.html', **context)