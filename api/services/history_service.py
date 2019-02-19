import os

from api.dto.history_dto import HistoryDTO
from api.repositories.history_repository import HistoryRepository
from api.services.domain_models.history_dm import HistoryDomainModel
from api.services.image_helper import ImageHelper
from api.services.mappings import mapper
from definitions import ROOT_DIR
from api.persistence.models.history import History


class HistoryService:

    def __init__(self, person_service):
        self.person_service = person_service
        self.history_repo = HistoryRepository()

    def get_recent_histories_dtos(self, n:int):
        historiesDTO = []
        historiesDM = self.get_recent_histories(n)
        for historyDM in historiesDM:
            person = self.person_service.get_person(historyDM.person_id)

            history_dto = HistoryDTO()
            history_dto.created_on = historyDM.created_on
            history_dto.matching_ratio = historyDM.matching_ratio
            history_dto.person_id = historyDM.person_id
            history_dto.username = historyDM.username
            history_dto.match_name = person.name
            history_dto.match_photo = ImageHelper.read_image_as_base64_string(os.path.join(ROOT_DIR, person.photo_uri))

            historiesDTO.append(history_dto)

        return historiesDTO


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
