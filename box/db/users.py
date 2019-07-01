
from ..models import User

class Users():
    def __init__(self, users_service):
        self._users_service = users_service

    def get(self, id: str) -> User:
        return self._users_service.get(id)
