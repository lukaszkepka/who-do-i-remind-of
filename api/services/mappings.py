from mapper.object_mapper import ObjectMapper
from api.persistence.models.dataset import Dataset
from api.persistence.models.history import History
from api.persistence.models.person import Person
from api.services.domain_models.dataset_dm import DatasetDomainModel
from api.services.domain_models.history_dm import HistoryDomainModel
from api.services.domain_models.person_dm import PersonDomainModel


mapper = ObjectMapper()

mapper.create_map(Dataset, DatasetDomainModel)
mapper.create_map(History, HistoryDomainModel)
mapper.create_map(Person, PersonDomainModel)

mapper.create_map(DatasetDomainModel, Dataset)
mapper.create_map(HistoryDomainModel, History)
mapper.create_map(PersonDomainModel, Person)
