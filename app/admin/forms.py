from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators
from app.core.models import Blog


class CreatePostForm(Form):
    title  = StringField('Title', [validators.InputRequired(message='Title can not empty')])
    author = StringField('Your Name', [validators.InputRequired(message='Name can not empty')])
    content = TextAreaField('Text', [validators.InputRequired(message='Content can not empty')])
    category = StringField('Your Post Category',
        [validators.InputRequired('Category of your Post can not empty'),
         validators.Regexp(message='Category must have only uppercase letters', regex=r'^[A-Z\d ]+$')
        ])

    