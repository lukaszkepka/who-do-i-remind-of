
class PhotoDatabaseDomainModel:

    def __init__(self, name=''):
        self.id = 0
        self.name = name

    def __repr__(self):
        return "<PhotoDatabaseDomainModel(Id=%ld, Name=%s)>" % (self.id, self.name)
