from api.persistence.base import Base
from sqlalchemy import BigInteger, Float, String
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class History(Base):
    __tablename__ = 'Histories'

    Id = Column(BigInteger, primary_key=True)
    Username = Column(String, nullable=False)
    MatchingRatio = Column(Float, nullable=False)
    PersonId = Column(BigInteger, ForeignKey('Persons.Id'), nullable=False)
    Person = relationship('Person', backref=backref('Histories', order_by=Id), foreign_keys=[PersonId])

    def __init__(self, username='', matching_ratio=0.0, person_id=0):
        self.Id = 0
        self.Username = username
        self.MatchingRatio = matching_ratio
        self.PersonId = person_id

    def __repr__(self):
        return "<History(Id=%ld, Username=%s, MatchingRatio=%f, PersonId=%d)>" \
               % (self.Id, self.Username, self.MatchingRatio, self.PersonId)
