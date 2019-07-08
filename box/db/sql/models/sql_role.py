from sqlalchemy import (
    Column,
    Integer,
    String
)

from flask_security import RoleMixin

from .. import db


class SQLRole(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
