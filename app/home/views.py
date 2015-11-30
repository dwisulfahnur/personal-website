from flask import Blueprint, render_template
from app.core.db import db
from app.core.models import *

home_views = Blueprint('home', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@home_views.route('/')
def home():
	personal_information = PersonalInformation.query.filter_by(full_name='Dwi Sulfahnur').first()
	return render_template('index.html', **locals())
