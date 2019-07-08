from ...models import Role

class RoleService():
    def __init__(self, role_service):
        self._role_service = role_service

    def get(self, id: str) -> Role:
        return self._role_service.get(id)
