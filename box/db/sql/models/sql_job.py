from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .. import db


class SQLJob(db.Model):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))

    owner = relationship('OwnerMixin')
