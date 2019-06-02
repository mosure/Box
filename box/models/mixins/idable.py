class IDableMixin(object):
    def __init__(self, id):
        self.id = id

        # Cast all of our IDs to a string (we can add different types in the future)
        if not isinstance(self.id, str):
            self.id = str(self.id)
