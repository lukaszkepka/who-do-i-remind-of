from mapper.object_mapper import ObjectMapper
from api.persistence.models.dataset import Dataset
from api.persistence.models.history import History
from api.persistence.models.person import Person
from api.services.domain_models.dataset_dm import DatasetDomainModel
from api.services.domain_models.history_dm import HistoryDomainModel
from api.services.domain_models.person_dm import PersonDomainModel


mapper = ObjectMapper()

mapper.create_map(Dataset, DatasetDomainModel)
mapper.create_map(History, HistoryDomainModel, {"person": lambda history: mapper.map(history.person, PersonDomainModel)})
mapper.create_map(Person, PersonDomainModel, {"dataset": lambda person: mapper.map(person.dataset, DatasetDomainModel),
                                              "birth_date": lambda person: person.birth_date.strftime('%Y-%m-%d')})

mapper.create_map(DatasetDomainModel, Dataset)
mapper.create_map(HistoryDomainModel, History)
mapper.create_map(PersonDomainModel, Person)
