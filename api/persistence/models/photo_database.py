from api.persistence.base import Base
from sqlalchemy import BigInteger, String
from sqlalchemy import Column


class PhotoDatabase(Base):
    __tablename__ = 'PhotoDatabases'

    id = Column('Id', BigInteger, primary_key=True)
    name = Column('Name', String, nullable=False)

    def __init__(self, name=''):
        self.id = None
        self.name = name

    def __repr__(self):
        return "<PhotoDatabase(Id=%ld, Name=%s)>" % (self.id, self.name)
