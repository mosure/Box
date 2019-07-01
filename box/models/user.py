import uuid

from .role import Role

from .mixins import (
    IDableMixin,
    MetadatableMixin,
    OwnerMixin
)

from flask_login import (
    UserMixin
)

class User(UserMixin, IDableMixin, MetadatableMixin, OwnerMixin):
    def __init__(self, email, fname, lname, jobs, parts, pwd, role):
        IDableMixin.__init__(self, uuid.uuid4())
        MetadatableMixin.__init__(self)
        OwnerMixin.__init__(self, jobs, parts)

        self.role = role
