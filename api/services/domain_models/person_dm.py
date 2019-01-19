
class PersonDomainModel:

    def __init__(self, name='', photo_uri='', model='', photo_database_id=0):
        self.id = 0
        self.name = name
        self.photo_uri = photo_uri
        self.model = model
        self.photo_database_id = photo_database_id
        self.photo_database = None

    def __repr__(self):
        return "<PersonDomainModel(Id=%ld, Name=%s, PhotoURI=%s, Model=%s, PhotoDatabaseId=%d)>" \
               % (self.id, self.name, self.photo_uri, self.model, self.photo_database_id)
