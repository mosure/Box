import os

from flask import Flask
from injector import (
    Binder,
    Module,
    singleton,
    provider
)

from .sql import initialize_database as sql_initialize_database
from .sql import db as sql_db
from .sql.services import (
    SQLJobService,
    SQLUserService,
    SQLRoleService
)

from .services.job_service import JobService
from .services.user_service import UserService
from .services.role_service import RoleService

from ..configuration import Configuration


class DatabaseModule(Module):
    """Configure database service providers"""
    
    @inject(app=Flask)
    @inject(configuration=Configuration)
    def __init__(self, app: Flask, configuration: Configuration):
        self._configuration = configuration

        if self._database == 'sql':
            sql_initialize_database(app, configuration)
        else:
            app.logger().error('DATABASE value is incorrect.')

    @singleton
    @provider(JobService)
    def provide_job_service(self):
        if self._configuration.database == 'sql':
            return JobService(SQLJobService(sql_db))

        return None

    @singleton
    @provider(UserService)
    def provide_user_service(self):
        if self._configuration.database == 'sql':
            return UserService(SQLUserService(sql_db))

        return None

    @singleton
    @provider(RoleService)
    def provide_role_service(self):
        if self._configuration.database == 'sql':
            return RoleService(SQLRoleService(sql_db))

        return None
