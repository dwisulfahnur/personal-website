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
         return '<Personal Information {}>'.format(self.id)


'''
class activities(db.Model):
	__tablename__ = 'activities'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	author = db.Column(db.String())
	content = db.Column(db.String())


    def __repr__(self):
         return 'activities {}>'.format(self.title)'''
