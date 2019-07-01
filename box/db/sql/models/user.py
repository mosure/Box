from sqlalchemy import Column, Integer

from .. import db


class Job(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
