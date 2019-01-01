
class PersonDomainModel:

    def __init__(self, name='', surname='', birthdate='', photoURI='', model='', dataset_id=0):
        self.Id = 0
        self.Name = name
        self.Surname = surname
        self.BirthDate = birthdate
        self.PhotoURI = photoURI
        self.Model = model
        self.DatasetId = dataset_id
        self.Dataset = None

    def __repr__(self):
        return "<PersonDomainModel(Id=%ld, Name=%s, Surname=%s, BirthDate=%s, PhotoURI=%s, Model=%s, DatasetId=%d)>" \
               % (self.Id, self.Name, self.Surname, self.BirthDate, self.PhotoURI, self.Model, self.DatasetId)
