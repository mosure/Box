import uuid

from .mixins import (
    CompletableMixin,
    IDableMixin,
    MetadatableMixin
)


class Operation(CompletableMixin, IDableMixin, MetadatableMixin):
    def __init__(self, id):
        CompletableMixin.__init__()
        IDableMixin.__init__(id)
        MetadatableMixin.__init__()
        