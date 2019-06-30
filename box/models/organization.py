from .mixins import (
    MetadatableMixin,
    OwnerMixin
)


class Organization(MetadatableMixin, OwnerMixin):
    def __init__(self, name, roles, users):
        MetadatableMixin.__init__(self)
        OwnerMixin.__init__(self, 'organization')

        self.roles = roles
        self.name = name
        self.users = users
