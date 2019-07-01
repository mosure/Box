from flask import (
    Blueprint,
    redirect,
    make_response,
    url_for
)

from flask_login import (
    login_required,
    logout_user,
    login_user
)

from injector import (
    inject
)

from ...db import Users

auth_bp = Blueprint('auth', __name__)

@inject(users=Users)
@jobs_bp.route('/login', methods=['POST'])
def login(users: Users):
    # TODO: Add some data validation here
    # login_user()
    pass

@jobs_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
