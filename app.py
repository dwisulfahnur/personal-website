from flask import Flask, render_template
from db import db
from models import PersonalInformation
from admin.views import admin_views
from activities.views import activities_views
from photos.views import photos_views
from blog.views import blog_views


app = Flask(__name__)

####blueprint########
app.register_blueprint(admin_views)
app.register_blueprint(activities_views)
app.register_blueprint(photos_views)
app.register_blueprint(blog_views)

app.config.from_object('config')
db.init_app(app)


@app.route('/')
def home():
    personal_information = PersonalInformation.query.filter_by(id=2).first()
    return render_template('index.html', **locals())

@app.errorhandler(404)
def page_not_found(error):
    personal_information = PersonalInformation.query.filter_by(id=2).first()
    return render_template('404.html', **locals()), 404

if __name__ == "__main__":
   app.run()