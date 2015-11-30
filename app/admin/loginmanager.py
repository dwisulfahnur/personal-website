from flask.ext.login import LoginManager
from app.admin.models import User

login_manager = LoginManager()

@login_manager.user_loader
def user_loader(user_id):
    return User.query.filter_by(id=user_id).first()

login_manager.login_view = '.admin_login'
