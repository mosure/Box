import uuid

from .mixins import (
    ChronoEdgeMixin,
    IDableMixin,
    MetadatableMixin
)

from .operation import Operation


class Job(ChronoEdgeMixin, IDableMixin, MetadatableMixin):
    def __init__(self):
        ChronoEdgeMixin.__init__(self)
        IDableMixin.__init__(self, uuid.uuid4())
        MetadatableMixin.__init__(self)

        self.operations = []
