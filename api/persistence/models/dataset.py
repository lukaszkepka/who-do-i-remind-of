from api.persistence.base import Base
from sqlalchemy import BigInteger, String
from sqlalchemy import Column


class Dataset(Base):
    __tablename__ = 'Datasets'

    Id = Column(BigInteger, primary_key=True)
    Name = Column(String, nullable=False)

    def __init__(self, name=''):
        self.Id = 0
        self.Name = name

    def __repr__(self):
        return "<Dataset(Id=%ld, Name=%s)>" % (self.Id, self.Name)
