from flask import Blueprint, render_template
from app.core.db import db
from app.core.models import *

photos_views = Blueprint('photos', __name__,
                        template_folder='../../templates',
                        static_folder='../../static')

@photos_views.route('/photos/')
def photos():
	posts = db.session.query(Photos).all()
	personal_information = PersonalInformation.query.filter_by(id=2).first()
	context = {	'posts' : posts,
				'personal_information' : personal_information
			  }
	return render_template('photos.html', **locals())