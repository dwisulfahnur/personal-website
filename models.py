import datetime
from db import db
from werkzeug.security import generate_password_hash



'''class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String())
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<Users{}>'.format(self.username)'''


class PersonalInformation(db.Model):
    __tablename__ = 'personal_information'

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String())
    avatar = db.Column(db.String())
    job = db.Column(db.String())
    organization = db.Column(db.String())
    address = db.Column(db.String())
    github = db.Column(db.String())
    facebook = db.Column(db.String())
    twitter = db.Column(db.String())
    no_hp = db.Column(db.String())

    def __repr__(self):
        return '<PersonalInformation{}>'.format(self.id)

class Activities(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    content = db.Column(db.String())

    def __init__(self, title, content):
        self.title = title
        self.content = content
            

    def __repr__(self):
        return '<activities{}>'.format(self.title)


class Photos(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String())
    url = db.Column(db.String())

    def __init__(self, label, url):
        self.label = label
        self.url = url


    def __repr__(self):
        return '<photos{}>'.format(self.label)