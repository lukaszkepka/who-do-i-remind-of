from api.repositories.history_repository import HistoryRepository
from api.services.domain_models.history_dm import HistoryDomainModel
from api.services.mappings import mapper
from api.persistence.models.history import History


class HistoryService:

    def __init__(self):
        self.history_repo = HistoryRepository()

    def get_recent_histories(self, n: int):
        histories = self.history_repo.get_histories(True, n)
        historiesDM = list()
        for history in histories:
            historiesDM.append(mapper.map(history, HistoryDomainModel))

        return historiesDM

    def add_history_entry(self, matches, user_name):
        if len(matches) < 1:
            raise Exception('Matches are empty')

        best_match = matches[0]
        history_entry = History()
        history_entry.person_id = best_match.person_id
        history_entry.matching_ratio = best_match.similarity_ratio
        history_entry.username = user_name

        self.history_repo.add_history(history_entry)
