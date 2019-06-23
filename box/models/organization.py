import uuid

from .mixins import (
    IDableMixin,
    MetadatableMixin,
    OwnerMixin
)

class Organization(IDableMixin, MetadatableMixin):
    def __init__(self, jobs, name, parts, roles, users):
        IDableMixin.__init__(self, uuid.uuid4())
        MetadatableMixin.__init__(self)
        OwnerMixin.__init__(self, jobs, parts)

        self.roles = roles
        self.name = name
        self.users = users
