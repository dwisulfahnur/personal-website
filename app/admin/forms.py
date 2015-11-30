from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, validators
from app.core.models import Blog

class LoginForm(Form):
    username = StringField('username', [validators.InputRequired(message='Please enter your Username here')])
    password = PasswordField('password', [validators.InputRequired(message='Please enter your Password here')])

class CreatePostForm(Form):
    title  = StringField('Title', [validators.InputRequired(message='Please enter Post Title')])
    author = StringField('Your Name', [validators.InputRequired(message='Please enter Your Name')])
    content = TextAreaField('Text', [validators.InputRequired(message='Please enter Post Content')])
    category = StringField('Your Post Category',
        [validators.InputRequired('Please enter Post Category'),
         validators.Regexp(message='Category must have only uppercase letters', regex=r'^[A-Z\d ]+$')
        ])

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        blog = Blog.query.filter_by(title = self.title.data).first()
        if blog:
            self.title.error = "Title already exist"
            return False
        return True

class UpdatePostForm(Form):
    title  = StringField('Title', [validators.InputRequired(message='Please enter Post Title')])
    author = StringField('Your Name', [validators.InputRequired(message='Please enter Your Name')])
    content = TextAreaField('Text', [validators.InputRequired(message='Please enter Post Content')])
    category = StringField('Your Post Category',
        [validators.InputRequired('Please enter Post Category'),
         validators.Regexp(message='Category must have only uppercase letters', regex=r'^[A-Z\d ]+$')
        ])
