from app.core.helper import create_app
from app.core.db import db

from app.home.views import home_views
from app.user.views import user_views
from app.activities.views import activities_views
from app.photos.views import photos_views
from app.blog.views import blog_views

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
db.init_app(app)

# register blueprint
app.register_blueprint(home_views)
app.register_blueprint(user_views)
app.register_blueprint(activities_views)
app.register_blueprint(photos_views)
app.register_blueprint(blog_views)