import os

from flask import (
    Flask,
    make_response,
    jsonify
)

from .v1 import register_blueprints
from .handlers import override_handlers


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, root_path='/box')

    register_blueprints(app)

    override_handlers(app)

    return app
