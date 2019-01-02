from api.repositories.history_repository import HistoryRepository
from api.services.domain_models.history_dm import HistoryDomainModel
from api.services.mappings import mapper


class HistoryService:

    def __init__(self):
        self.history_repo = HistoryRepository()

    def get_recent_histories(self, n: int):
        histories = self.history_repo.get_histories(True, n)
        historiesDM = list()
        for history in histories:
            historiesDM.append(mapper.map(history, HistoryDomainModel))

        return historiesDM

