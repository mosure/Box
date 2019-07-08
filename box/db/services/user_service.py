from ...models import User

class UserService():
    def __init__(self, user_service):
        self._user_service = user_service

    def get(self, id: str) -> User:
        return self._user_service.get(id)
