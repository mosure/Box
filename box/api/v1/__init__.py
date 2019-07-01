from flask import (
    Blueprint,
    jsonify,
    request,
    abort,
    make_response
)

from .auth import auth_bp
from .blueprints import blueprints_bp
from .jobs import jobs_bp
from .operations import operations_bp


API_BASE_URL = '/api/v1/'

def register_blueprints(app):
    app.register_blueprint(blueprints_bp, url_prefix=API_BASE_URL + 'blueprints')
    app.register_blueprint(jobs_bp, url_prefix=API_BASE_URL + 'jobs')
    app.register_blueprint(operations_bp, url_prefix=API_BASE_URL + 'operations')
    app.register_blueprint(auth_bp, url_prefix=API_BASE_URL)