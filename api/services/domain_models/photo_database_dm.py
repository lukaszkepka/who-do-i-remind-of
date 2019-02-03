
class PhotoDatabaseDomainModel:

    def __init__(self, name='', description=''):
        self.id = None
        self.name = name
        self.description = description

    def __repr__(self):
        return "<PhotoDatabaseDomainModel(Id=%ld, Name=%s, Description=%s)>" % (self.id, self.name, self.description)
