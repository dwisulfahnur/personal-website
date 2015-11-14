from datetime import date
from db import db




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
        return '<PersonalInformation: {}>'.format(self.id)

class Activities(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    created = db.Column(db.String())

    def __init__(self, title, content, created):
        self.title = title
        self.content = content
        if self.id == None:
            now = date.today()
            self.created = '%d/%d/%d' % (now.day, now.month, now.year)
            

    def __repr__(self):
        return '<activities: {}>'.format(self.title)


class Photos(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String())
    url = db.Column(db.String())

    def __init__(self, label, url):
        self.label = label
        self.url = url


    def __repr__(self):
        return '<photos: {}>'.format(self.label)



class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name_category = db.Column(db.String())
    created = db.Column(db.String())

    def __init__(self, name_category):
        self.name_category = name_category
        if self.id == None:
            now = date.today()
            self.created = '%d/%d/%d' % (now.day, now.month, now.year)
    def __repr__(self):
        return '{}'.format(self.name_category)

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    content = db.Column(db.String())
    created = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    category = db.relationship('Category',
        backref= db.backref('blog', lazy='dynamic'))
    

    def __init__(self, title, author, content, category_id):
        self.title = title
        self.author = author
        self.content = content
        self.category_id = category_id
        
        if self.id == None:
            now = date.today()
            self.created = '%d/%d/%d' % (now.day, now.month, now.year)
    def __repr__(self):
        return '<Blog: {}>'.format(self.title)