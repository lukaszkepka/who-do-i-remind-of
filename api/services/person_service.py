from api.persistence.models.person import Person
from api.services.domain_models.person_dm import PersonDomainModel
from api.services.mappings import mapper


class PersonService:

    def __init__(self, person_repository):
        self.person_repository = person_repository

    def add_or_update_person(self, person_dm):
        if type(person_dm) is not PersonDomainModel:
            raise Exception("Wrong parameter type: person_dm")
        person = mapper.map(person_dm, Person)
        try:
            existing_person = self.person_repository.get_person_by_name(person.name)
            if existing_person is None:
                self.person_repository.add_person(person)
            else:
                person.id = existing_person.id
                self.person_repository.update_person(person)
        except Exception as ex:
            print(ex)

