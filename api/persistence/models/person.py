from api.persistence.base import Base
from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class Person(Base):
    __tablename__ = 'Persons'

    id = Column('Id', BigInteger, primary_key=True)
    name = Column('Name', String, nullable=False)
    surname = Column('Surname', String, nullable=False)
    birth_date = Column('BirthDate', DateTime)
    photo_uri = Column('PhotoURI', String, nullable=False)
    model = Column('Model', String, nullable=False)
    dataset_id = Column('DatasetId', BigInteger, ForeignKey('Datasets.Id'), nullable=False)
    dataset = relationship('Dataset', backref=backref('persons', order_by=id), foreign_keys=[dataset_id])

    def __init__(self, name='', surname='', birthdate='', photoURI='', model='', dataset_id=0):
        self.id = 0
        self.name = name
        self.surname = surname
        self.birth_date = birthdate
        self.photo_uri = photoURI
        self.model = model
        self.dataset_id = dataset_id

    def __repr__(self):
        return "<Person(Id=%ld, Name=%s, Surname=%s, BirthDate=%s, PhotoURI=%s, Model=%s, DatasetId=%d)>" \
               % (self.id, self.name, self.surname, self.birth_date, self.photo_uri, self.model, self.dataset_id)
