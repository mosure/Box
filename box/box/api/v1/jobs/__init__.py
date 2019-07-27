"""Jobs blueprint"""
from flask import Blueprint

jobs_blueprint = Blueprint('jobs', __name__)

from . import routes
