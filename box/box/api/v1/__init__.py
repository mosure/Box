from flask_apispec import FlaskApiSpec

from .blueprints import blueprints_blueprint
from .jobs import jobs_blueprint
from .operations import operations_blueprint


API_BASE_URL = '/api/v1/'

def register_blueprints(app):
    app.register_blueprint(blueprints_blueprint, url_prefix=API_BASE_URL + 'blueprints')
    app.register_blueprint(jobs_blueprint, url_prefix=API_BASE_URL + 'jobs')
    app.register_blueprint(operations_blueprint, url_prefix=API_BASE_URL + 'operations')


    # Swagger
    docs = FlaskApiSpec(app)

    from .jobs.routes import get_job

    docs.register(get_job, blueprint="jobs")
