from flask import (
    Blueprint,
    jsonify,
    request,
    abort,
    make_response
)

from .blueprints import blueprints_bp
from .jobs import jobs_bp
from .operations import operations_bp


def register_blueprints(app):
    app.register_blueprint(blueprints_bp, url_prefix='/api/v1/blueprints')
    app.register_blueprint(jobs_bp, url_prefix='/api/v1/jobs')
    app.register_blueprint(operations_bp, url_prefix='/api/v1/operations')
