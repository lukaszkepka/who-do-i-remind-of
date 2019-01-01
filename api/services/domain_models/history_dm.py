
class HistoryDomainModel:

    def __init__(self, username='', matching_ratio=0.0, person_id=0):
        self.Id = 0
        self.Username = username
        self.MatchingRatio = matching_ratio
        self.PersonId = person_id
        self.Person = None

    def __repr__(self):
        return "<HistoryDomainModel(Id=%ld, Username=%s, MatchingRatio=%f, PersonId=%d)>" \
               % (self.Id, self.Username, self.MatchingRatio, self.PersonId)
