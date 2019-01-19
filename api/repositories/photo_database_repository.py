from api.persistence.models.photo_database import PhotoDatabase
from api.repositories.base_repository import BaseRepository


class PhotoDatabaseRepository(BaseRepository):

    def add_photo_database(self, photo_database):
        if type(photo_database) is not PhotoDatabase:
            return
        session = BaseRepository.get_session(self)
        session.add(photo_database)
        session.commit()

    def update_photo_database(self, updated_photo_database):
        if type(updated_photo_database) is not PhotoDatabase:
            return
        session = BaseRepository.get_session(self)
        photo_database = session.query(PhotoDatabase).filter_by(Id=updated_photo_database.Id).first()
        properties = dir(photo_database)
        for prop in properties:
            if prop != 'Id' and not prop.startswith('_') and not prop.endswith('_'):
                setattr(photo_database, prop, getattr(updated_photo_database, prop))

        session.commit()

    def get_photo_database(self, id):
        session = BaseRepository.get_session(self)
        photo_database = session.query(PhotoDatabase).filter_by(Id=id).first()
        return photo_database

    def get_photo_databases(self, query=True):
        session = BaseRepository.get_session(self)
        photo_databases = session.query(PhotoDatabase).filter(query).all()
        return list(photo_databases)

