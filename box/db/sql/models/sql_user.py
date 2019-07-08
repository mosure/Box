from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String
)
from sqlalchemy.orm import (
    relationship,
    backref
)

from flask_security import UserMixin

from .. import db


class SQLUser(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))
