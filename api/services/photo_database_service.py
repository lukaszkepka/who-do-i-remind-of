import os

from api.dto.photo_database_example_dto import PhotoDatabaseExampleDto
from api.persistence.models.photo_database import PhotoDatabase
from api.services.domain_models.photo_database_dm import PhotoDatabaseDomainModel
from api.services.image_helper import ImageHelper
from api.services.mappings import mapper
import random

from definitions import ROOT_DIR


class PhotoDatabaseService:

    def __init__(self, photo_database_repository, person_repository):
        self.photo_database_repository = photo_database_repository
        self.person_repository = person_repository

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

    def get_photo_databases_with_examples(self, photo_examples_count):
        try:
            photo_db_example_dto_collection = []
            photo_databases = self.photo_database_repository.get_photo_databases()
            for photo_database in photo_databases:
                photo_database_example_dto = PhotoDatabaseExampleDto(photo_database.id, photo_database.name)
                persons = self.person_repository.get_persons(photo_database.id)
                max_index = len(persons) - 1
                if max_index > 1:
                    for i in range(1, photo_examples_count + 1):
                        random_index = random.randint(1, max_index)
                        person = persons[random_index]
                        image_base64 = ImageHelper.read_image_as_base64_string(os.path.join(ROOT_DIR, person.photo_uri))
                        photo_database_example_dto.photos.append(image_base64)

                photo_db_example_dto_collection.append(photo_database_example_dto)
            return photo_db_example_dto_collection
        except Exception as ex:
            print(ex)




