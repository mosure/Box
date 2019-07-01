from flask_login import (
    LoginManager,
)

from .user import User
from ..db import Users

class Auth:
    @inject(app=Flask)
    def __init__(self, app: Flask):
        self.login_manager = LoginManager()
        self.login_manager.init_app(app)

    @inject(users=Users)
    @login_manager.user_loader
    def load_user(user_id, users: Users):
        return Users.get(user_id)
