from .role import Role

from .mixins import (
    MetadatableMixin,
    OwnerMixin
)

from flask_login import (
    UserMixin
)

class User(UserMixin, MetadatableMixin, OwnerMixin):
    def __init__(self, email, fname, lname, pwd, role):
        MetadatableMixin.__init__(self)
        OwnerMixin.__init__(self, 'user')

        self.fname = fname
        self.lname = lname
        self.email = email
        self.pwd = pwd
        self.role = role
