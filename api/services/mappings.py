from mapper.object_mapper import ObjectMapper
from api.persistence.models.photo_database import PhotoDatabase
from api.persistence.models.history import History
from api.persistence.models.person import Person
from api.services.domain_models.photo_database_dm import PhotoDatabaseDomainModel
from api.services.domain_models.history_dm import HistoryDomainModel
from api.services.domain_models.person_dm import PersonDomainModel


mapper = ObjectMapper()

mapper.create_map(PhotoDatabase, PhotoDatabaseDomainModel)
mapper.create_map(History, HistoryDomainModel, {"person": lambda history: mapper.map(history.person, PersonDomainModel)})
mapper.create_map(Person, PersonDomainModel,
                  {"photo_database": lambda person: mapper.map(person.photo_database, PhotoDatabaseDomainModel)})

mapper.create_map(PhotoDatabaseDomainModel, PhotoDatabase)
mapper.create_map(HistoryDomainModel, History)
mapper.create_map(PersonDomainModel, Person)
