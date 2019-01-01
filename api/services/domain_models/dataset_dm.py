
class DatasetDomainModel:

    def __init__(self, name=''):
        self.Id = 0
        self.Name = name

    def __repr__(self):
        return "<DatasetDomainModel(Id=%ld, Name=%s)>" % (self.Id, self.Name)
