from api.persistence.base import Base
from sqlalchemy import BigInteger, String, LargeBinary
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class Person(Base):
    __tablename__ = 'Persons'

    id = Column('Id', BigInteger, primary_key=True)
    name = Column('Name', String, nullable=False)
    photo_uri = Column('PhotoURI', String, nullable=False)
    model = Column('Model', LargeBinary, nullable=False)
    photo_database_id = Column('PhotoDatabaseId', BigInteger, ForeignKey('PhotoDatabases.Id'), nullable=False)
    _photo_database = relationship('PhotoDatabase', backref=backref('_persons', order_by=id),
                                   foreign_keys=[photo_database_id])

    def __init__(self, name='', photo_uri='', model='', photo_database_id=0):
        self.id = None
        self.name = name
        self.photo_uri = photo_uri
        self.model = model
        self.photo_database_id = photo_database_id
