from api.persistence.models.photo_database import PhotoDatabase
from api.services.domain_models.photo_database_dm import PhotoDatabaseDomainModel
from api.services.mappings import mapper


class PhotoDatabaseService:

    def __init__(self, photo_database_repository):
        self.photo_database_repository = photo_database_repository

    def add_or_update_photo_database(self, photo_database_dm):
        if type(photo_database_dm) is not PhotoDatabaseDomainModel:
            raise Exception("Wrong parameter type: photo_database_dm")
        photo_database = mapper.map(photo_database_dm, PhotoDatabase)
        try:
            existing_photo_database = self.photo_database_repository.get_photo_database_by_name(photo_database.name)
            if existing_photo_database is None:
                self.photo_database_repository.add_photo_database(photo_database)
            else:
                photo_database.id = existing_photo_database.id
                self.photo_database_repository.update_photo_database(photo_database)
        except Exception as ex:
            print(ex)

    def get_photo_database_by_name(self, name):
        try:
            return self.photo_database_repository.get_photo_database_by_name(name)
        except Exception as ex:
            print(ex)
