from .owner import OwnerMixin


class OwnableMixin(object):
    def __init__(self, owner):
        self.owner = owner

        if isinstance(self.owner, OwnerMixin):
            self.owner = self.owner
