from api.persistence.base import Base
from sqlalchemy import BigInteger, String
from sqlalchemy import Column


class PhotoDatabase(Base):
    __tablename__ = 'PhotoDatabases'

    id = Column('Id', BigInteger, primary_key=True)
    name = Column('Name', String, nullable=False)
    description = Column('Description', String, nullable=True)

    def __init__(self, name='', description=''):
        self.id = None
        self.name = name
        self.description = description
