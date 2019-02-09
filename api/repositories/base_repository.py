from api.persistence.database_init import DatabaseConfig


class BaseRepository:

    def get_session(self):
        if DatabaseConfig.session_factory is None:
            raise Exception('Db session factory not initialized!')
        return DatabaseConfig.session_factory()

