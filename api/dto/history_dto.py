
class HistoryDTO:

    def __init__(self, username='', user_photo='', matching_ratio=0.0, person_id=0, match_photo='', match_name=''):
        self.username = username
        self.user_photo = user_photo
        self.matching_ratio = matching_ratio
        self.person_id = person_id
        self.match_name = match_name
        self.match_photo = match_photo
