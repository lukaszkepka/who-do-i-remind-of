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
        history = session.query(History).filter_by(id=updated_history.id).first()
        properties = dir(history)
        for prop in properties:
            if prop != 'id' and not prop.startswith('_') and not prop.endswith('_'):
                setattr(history, prop, getattr(updated_history, prop))

        session.commit()

    def get_history(self, id):
        session = BaseRepository.get_session(self)
        history = session.query(History).filter_by(id=id).first()
        return history

    def get_histories(self, query=True, n=-1):
        session = BaseRepository.get_session(self)
        if n == -1:
            histories = session.query(History).filter(query).all()
        else:
            histories = session.query(History).filter(query).limit(n).all()

        return list(histories)
