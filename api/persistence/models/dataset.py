from api.persistence.base import Base
from sqlalchemy import BigInteger, String
from sqlalchemy import Column


class Dataset(Base):
    __tablename__ = 'Datasets'

    id = Column('Id', BigInteger, primary_key=True)
    name = Column('Name', String, nullable=False)

    def __init__(self, name=''):
        self.id = 0
        self.name = name

    def __repr__(self):
        return "<Dataset(Id=%ld, Name=%s)>" % (self.id, self.name)
