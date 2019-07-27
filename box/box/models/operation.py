import uuid

from .mixins import (
    CompletableMixin,
    IDableMixin,
    MetadatableMixin
)


class Operation(CompletableMixin, IDableMixin, MetadatableMixin):
    def __init__(self, id):
        CompletableMixin.__init__(self)
        IDableMixin.__init__(self, id)
        MetadatableMixin.__init__(self)
        