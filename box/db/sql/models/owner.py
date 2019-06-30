from sqlalchemy import Column, Integer, String

from .. import db


class Owner(db.Model):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    type = Column(String)
