
class HistoryDomainModel:

    def __init__(self, username='', matching_ratio=0.0, person_id=0, user_image_base64=''):
        self.id = None
        self.username = username
        self.matching_ratio = matching_ratio
        self.person_id = person_id
        self.user_image_base64 = user_image_base64

    def __repr__(self):
        return "<HistoryDomainModel(Id=%ld, Username=%s, MatchingRatio=%f, PersonId=%d)>" \
               % (self.id, self.username, self.matching_ratio, self.person_id)
