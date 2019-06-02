from .idable import IDableMixin


class ChronoEdgeMixin(object):
    def __init__(self, next=None):
        self.next = next

        if not isinstance(self.next, list):
            self.next = [self.next]
        
        # Make sure we have a list of IDables
        for i in range(self.next):
            if not isinstance(self.next[i], IDableMixin):
                self.next[i] = IDableMixin(self.next[i])
