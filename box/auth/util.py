from flask_security.utils import (
    hash_password,
)

from flask_security.forms import (
    RegisterForm
)

from injector import (
    inject
)

from . import Auth

@inject(auth=Auth)
def create_user(auth: Auth, *args, **kwargs):
    form = RegisterForm(args, kwargs)
    if form.validate():
        kwargs['password'] = hash_password(kwargs['password'])
        auth.datastore.create_user(kwargs)
        auth.datastore.commit()
        return True
    return False
