from .role import Role

from .mixins import (
    MetadatableMixin,
    OwnerMixin
)

class User(MetadatableMixin, OwnerMixin):
    def __init__(self, *args, **kwargs):
        MetadatableMixin.__init__(self)
        OwnerMixin.__init__(self, 'user')
