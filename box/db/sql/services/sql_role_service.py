from ....models import Role


class SQLRoleService():
    """SQL Implementation of box.db.role"""

    def __init__(self, db):
        self._db = db

    def get(self, id: str) -> Role:
        return None
