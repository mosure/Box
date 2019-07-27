"""Operations blueprint"""
from flask import Blueprint

operations_blueprint = Blueprint('operations', __name__)

from . import routes
