from api.persistence.base import Base
from sqlalchemy import BigInteger, Float, String, DateTime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
import datetime


class History(Base):
    __tablename__ = 'Histories'

    id = Column('Id', BigInteger, primary_key=True)
    created_on = Column('CreatedOn', DateTime, nullable=False)
    username = Column('Username', String, nullable=False)
    matching_ratio = Column('MatchingRatio', Float, nullable=False)
    user_image_base64 = Column('UserImageBase64', String, nullable=False)
    person_id = Column('PersonId', BigInteger, ForeignKey('Persons.Id'), nullable=False)
    _person = relationship('Person', backref=backref('_histories', order_by=id), foreign_keys=[person_id])

    def __init__(self, username='', matching_ratio=0.0, person_id=0, user_image_base64=''):
        self.id = None
        self.username = username
        self.matching_ratio = matching_ratio
        self.person_id = person_id
        self.user_image_base64 = user_image_base64
        self.created_on = datetime.datetime.now()
