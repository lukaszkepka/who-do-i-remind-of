
class PersonDomainModel:

    def __init__(self, name='', surname='', birth_date='', photo_uri='', model='', dataset_id=0):
        self.id = 0
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.photo_uri = photo_uri
        self.model = model
        self.dataset_id = dataset_id
        self.dataset = None

    def __repr__(self):
        return "<PersonDomainModel(Id=%ld, Name=%s, Surname=%s, BirthDate=%s, PhotoURI=%s, Model=%s, DatasetId=%d)>" \
               % (self.id, self.name, self.surname, self.birth_date, self.photo_uri, self.model, self.dataset_id)
