from flask import (
    Blueprint,
    redirect,
    make_response,
    url_for
)

from flask_security import (
    login_required,
    LoginForm,
    login_user,
    logout_user,
    RegisterForm
)

from injector import (
    inject
)

from ...auth.util import create_user

auth_bp = Blueprint('auth', __name__)

@jobs_bp.route('/login', methods=['POST'])
def login(user_service: UserService):
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(form.next or url_for('index'))

@jobs_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@job_bp.route('/register', methods=['POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user(form.to_dict())
        return redirect(form.next or url_for('index'))
