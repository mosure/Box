import os

from flask import Flask
from injector import (
    Binder,
    Module,
    singleton
)

from .sql import initialize_database as sql_initialize_database
from .sql import db as sql_db
from .sql.services import (
    sql_job_service,
    sql_user_service
)

from .services.job_service import JobService
from .services.user_service import UserService

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
    @provides(JobService)
    def provide_job_service(self):
        if self._configuration.database == 'sql':
            return JobService(sql_job_service(sql_db))

        return None

    @singleton
    @provides(UserService)
    def provide_user_service(self):
        if self._configuration.database == 'sql':
            return UserService(sql_user_service(sql_db))

        return None
