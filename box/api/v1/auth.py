from flask import (
    Blueprint,
    redirect,
    make_response,
    url_for
)

from injector import (
    inject
)

from ...db.services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@inject(user_service=UserService)
@jobs_bp.route('/login', methods=['POST'])
def login(user_service: UserService):
    pass

@jobs_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    return redirect(url_for('login'))
