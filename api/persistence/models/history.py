from api.persistence.base import Base
from sqlalchemy import BigInteger, Float, String
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class History(Base):
    __tablename__ = 'Histories'

    id = Column('Id', BigInteger, primary_key=True)
    username = Column('Username', String, nullable=False)
    matching_ratio = Column('MatchingRatio', Float, nullable=False)
    person_id = Column('PersonId', BigInteger, ForeignKey('Persons.Id'), nullable=False)
    person = relationship('Person', backref=backref('histories', order_by=id), foreign_keys=[person_id])

    def __init__(self, username='', matching_ratio=0.0, person_id=0):
        self.id = None
        self.username = username
        self.matching_ratio = matching_ratio
        self.person_id = person_id

    def __repr__(self):
        return "<History(Id=%ld, Username=%s, MatchingRatio=%f, PersonId=%d)>" \
               % (self.id, self.username, self.matching_ratio, self.person_id)
