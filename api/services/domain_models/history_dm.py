
class HistoryDomainModel:

    def __init__(self, username='', matching_ratio=0.0, person_id=0):
        self.id = 0
        self.username = username
        self.matching_ratio = matching_ratio
        self.person_id = person_id
        self.person = None

    def __repr__(self):
        return "<HistoryDomainModel(Id=%ld, Username=%s, MatchingRatio=%f, PersonId=%d)>" \
               % (self.id, self.username, self.matching_ratio, self.person_id)
