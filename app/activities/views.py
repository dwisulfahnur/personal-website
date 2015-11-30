from flask import Blueprint, render_template
from app.core.db import db
from app.core.models import *

activities_views = Blueprint('activities', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@activities_views.route('/activities/')
def activities():
	posts = db.session.query(Activities).all()
	return render_template('activities.html', posts=posts)
