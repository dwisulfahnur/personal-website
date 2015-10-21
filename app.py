from flask import Flask, render_template
from db import db
from models import PersonalInformation

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)



@app.route('/')
def home():
    personal_information = PersonalInformation.query.filter_by(id=2).first()
    return render_template('index.html', **locals())


@app.route('/activities/')
def activities():
    personal_information = PersonalInformation.query.filter_by(id=2).first()
    return render_template('activities.html', **locals())

@app.route('/photos/')
def photos():
    personal_information = PersonalInformation.query.filter_by(id=2).first()
    return render_template('photos.html', **locals())



if __name__ == "__main__":
   app.run()


