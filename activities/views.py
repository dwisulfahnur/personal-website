from flask import Blueprint, render_template
from db import db
from models import *

activities_views = Blueprint('activities', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@activities_views.route('/activities/')
def activities():
	posts = db.session.query(Activities).all()
	personal_information = PersonalInformation.query.filter_by(id=2).first()
	context = {	'posts' : posts,
				'personal_information' : personal_information
			  }
	return render_template('activities.html', **context)