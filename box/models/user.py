import uuid

from .role import Role

from .mixins import (
    IDableMixin,
    MetadatableMixin,
    OwnerMixin
)

class User(IDableMixin, MetadatableMixin, OwnerMixin):
    def __init__(self, email, fname, lname, jobs, parts, pwd, role):
        IDableMixin.__init__(self, uuid.uuid4())
        MetadatableMixin.__init__(self)
        OwnerMixin.__init__(self, jobs, parts)

        self.fname = fname
        self.lname = lname
        self.email = email
        self.pwd = pwd
        self.role = role

        
