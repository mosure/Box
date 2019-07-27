from neo4j import GraphDatabase

from flask_injector import (
    Module,
    request,
    singleton
)

from .services import (
    JobService,
    RoleService,
    UserService
)

class DatabaseModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        self._driver = self.configure_database()
        binder.bind(GraphDatabase, to=self._driver, scope=singleton)
        self.configure_services(binder)

    def configure_database(self):
        driver = GraphDatabase.driver(
            self.app.config['DATABASE_URI'],
            auth=(
                self.app.config['DATABASE_USERNAME'],
                self.app.config['DATABASE_PASSWORD']
            )
        )

        # do some configuration?

        return driver

    def configure_services(self, binder):
        binder.bind(JobService, to=JobService(self._driver), scope=request)
        binder.bind(RoleService, to=RoleService(self._driver), scope=request)
        binder.bind(UserService, to=UserService(self._driver), scope=request)
