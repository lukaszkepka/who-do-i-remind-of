from datetime import datetime


class HistoryDTO:

    def __init__(self, username='', matching_ratio=0.0, person_id=0, created_on = 0, match_photo = '', match_name = ''):
        self.id = None
        self.username = username
        self.matching_ratio = matching_ratio
        self.person_id = person_id
        self.match_name = match_name
        self.match_photo = match_photo
        self.created_on = created_on

