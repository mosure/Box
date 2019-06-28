import os

from flask import Flask
from injector import (
    Binder,
    Module,
    singleton
)

from .sql import initialize_database as sql_initialize_database
from .sql import db as sql_db
from .sql import Jobs as sql_jobs

from .jobs import Jobs

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
    @provides(Jobs)
    def provide_jobs(self):
        if self._configuration.database == 'sql':
            return Jobs(sql_jobs(sql_db))

        return None
