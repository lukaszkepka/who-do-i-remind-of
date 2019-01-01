from api.persistence.models.history import History
from api.repositories.base_repository import BaseRepository


class HistoryRepository(BaseRepository):

    def add_history(self, history):
        if type(history) is not History:
            return
        session = BaseRepository.get_session(self)
        session.add(history)
        session.commit()

    def update_history(self, updated_history):
        if type(updated_history) is not History:
            return
        session = BaseRepository.get_session(self)
        history = session.query(History).filter_by(Id=updated_history.Id).first()
        properties = dir(history)
        for prop in properties:
            if prop != 'Id' and not prop.startswith('_') and not prop.endswith('_'):
                setattr(history, prop, getattr(updated_history, prop))

        session.commit()

    def get_history(self, id):
        session = BaseRepository.get_session(self)
        history = session.query(History).filter_by(Id=id).first()
        return history

    def get_histories(self, query=True):
        session = BaseRepository.get_session(self)
        histories = session.query(History).filter(query).all()
        return list(histories)
