import uuid

from .idable import IDableMixin


class OwnerMixin(IDableMixin):
    def __init__(self, owner_type):
        IDableMixin.__init__(self, uuid.uuid4())

        # This should be either organization or user
        self.type = owner_type
