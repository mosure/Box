import click
import os

from flask import Flask
from flask.cli import AppGroup
from flask_injector import FlaskInjector

from .api import override_handlers
from .api.v1 import register_blueprints

from .db import DatabaseModule

from .config import (
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configure app
    env = os.environ.get('FLASK_ENV', default='development')
    if env.lower() == 'development':
        app.config.from_object(DevelopmentConfig)
    elif env.lower() == 'testing':
        app.config.from_object(TestingConfig)
    elif env.lower() == 'production':
        app.config.from_object(ProductionConfig)

    # Override with instance specific configs
    try:
        app.config.from_pyfile('config.py')
    except IOError:
        app.logger.warning('Could not find instance/config.py, environment only suitable for development.')

    register_blueprints(app)
    override_handlers(app)

    return app

app = create_app()

# Register dependencies
FlaskInjector(app=app, modules=[DatabaseModule(app)])

# Box CLI Setup
user_cli = AppGroup('user')
app.cli.add_command(user_cli)

@user_cli.command('create')
@click.argument('name')
def create_user(name):
    """TODO: Call `flask user create <name>` to create a user"""
    pass

