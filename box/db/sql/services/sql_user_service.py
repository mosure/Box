from ....models import User


class SQLUserService():
    """SQL Implementation of box.db.users"""

    def __init__(self, db):
        self._db = db

    def get(self, id: str) -> User:
        return None