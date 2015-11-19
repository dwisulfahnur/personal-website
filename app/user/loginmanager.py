from flask.ext.login import LoginManager
from models import User

login_manager = LoginManager()
login_manager.login_view = '.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()