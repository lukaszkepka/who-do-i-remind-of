
class DatasetDomainModel:

    def __init__(self, name=''):
        self.id = 0
        self.name = name

    def __repr__(self):
        return "<DatasetDomainModel(Id=%ld, Name=%s)>" % (self.id, self.name)
