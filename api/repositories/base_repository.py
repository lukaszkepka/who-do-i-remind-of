from api.persistence.database_init import DatabaseInitialization


class BaseRepository:

    def get_session(self):
        return DatabaseInitialization.create_session()

