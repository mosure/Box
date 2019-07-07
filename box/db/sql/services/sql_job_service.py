from ....models import Job


class SQLJobService():
    """SQL Implementation of box.db.jobs"""

    def __init__(self, db):
        self._db = db

    def get(self, id: str) -> Job:
        return None
