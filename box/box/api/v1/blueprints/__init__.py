"""Bluprints blueprint"""
from flask import Blueprint

blueprints_blueprint = Blueprint('blueprints', __name__)

from . import routes
