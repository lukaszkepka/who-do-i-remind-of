from api.persistence.base import Base
from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class Person(Base):
    __tablename__ = 'Persons'

    Id = Column(BigInteger, primary_key=True)
    Name = Column(String, nullable=False)
    Surname = Column(String, nullable=False)
    BirthDate = Column(DateTime)
    PhotoURI = Column(String, nullable=False)
    Model = Column(String, nullable=False)
    DatasetId = Column(BigInteger, ForeignKey('Datasets.Id'), nullable=False)
    Dataset = relationship('Dataset', backref=backref('Persons', order_by=Id), foreign_keys=[DatasetId])

    def __init__(self, name, surname, birthdate, photoURI, model, dataset_id):
        self.Name = name
        self.Surname = surname
        self.BirthDate = birthdate
        self.PhotoURI = photoURI
        self.Model = model
        self.DatasetId = dataset_id
