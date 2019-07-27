class CompletableMixin(object):
    def __init__(self, qty=0, qty_complete=0):
        self.qty = qty
        self.qty_complete = qty_complete
