import click
from flask.cli import AppGroup
from flask_injector import FlaskInjector

from .auth import AuthModule
from .configuration import ConfigurationModule
from .db import DatabaseModule
from .api import create_app
from .auth import *
from .models import *
from .tests import *


app = create_app()

# Register dependencies
FlaskInjector(app=app, modules=[AuthModule, ConfigurationModule, DatabaseModule(app)])

# Box CLI Setup
user_cli = AppGroup('user')
app.cli.add_command(user_cli)

@user_cli.command('create')
@click.argument('name')
def create_user(name):
    """TODO: Call `flask user create <name>` to create a user"""
    pass
