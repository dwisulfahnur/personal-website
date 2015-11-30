from flask import render_template
from app.core.helper import create_app
from app.core.db import db
from app.admin.loginmanager import login_manager

from app.home.views import home_views
from app.activities.views import activities_views
from app.photos.views import photos_views
from app.blog.views import blog_views
from app.admin.views import admin_views

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'
app = create_app(config)

#initializing flask app
db.init_app(app)
login_manager.init_app(app)

# register blueprint
app.register_blueprint(admin_views)
app.register_blueprint(home_views)
app.register_blueprint(activities_views)
app.register_blueprint(photos_views)
app.register_blueprint(blog_views)
app.register_blueprint(admin_views)
