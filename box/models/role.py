import uuid

from .mixins import (
    IDableMixin,
    MetadatableMixin
)

class Role(IDableMixin, MetadatableMixin):
    def __init(self, role_id):
        IDableMixin.__init__(self, uuid.uuid4())
        MetadatableMixin.__init__(self)

        self.role_id = role_id
