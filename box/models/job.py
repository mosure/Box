import uuid

from .mixins import (
    ChronoEdgeMixin,
    IDableMixin,
    MetadatableMixin
)

from .operation import Operation


class Job(ChronoEdgeMixin, IDableMixin, MetadatableMixin):
    def __init__(self):
        ChronoEdgeMixin.__init__()
        IDableMixin.__init__(uuid.uuid4())
        MetadatableMixin.__init__()

        self.operations = []
