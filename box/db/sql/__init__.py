from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from ...configuration import Configuration

db = None

def initialize_database(app: Flask, configuration: Configuration):
    """This could be better but gives us a 'root' level for database models"""

    global db

    app.config['SQLALCHEMY_DATABASE_URI'] = configuration.database_uri
    db = SQLAlchemy(app)
