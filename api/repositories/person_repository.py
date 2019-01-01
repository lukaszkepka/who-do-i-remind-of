from api.persistence.database_init import DatabaseInitialization
from api.persistence.models.person import Person
from api.repositories.base_repository import BaseRepository


class PersonRepository(BaseRepository):

    def get_session(self):
        return DatabaseInitialization.create_session()

    def add_person(self, person):
        if type(person) is not Person:
            return
        session = BaseRepository.get_session(self)
        session.add(person)
        session.commit()

    def update_person(self, updated_person):
        if type(updated_person) is not Person:
            return
        session = BaseRepository.get_session(self)
        person = session.query(Person).filter_by(Id=updated_person.Id).first()
        properties = dir(person)
        for prop in properties:
            if prop != 'Id' and not prop.startswith('_') and not prop.endswith('_'):
                setattr(person, prop, getattr(updated_person, prop))

        session.commit()

    def get_person(self, id):
        session = BaseRepository.get_session(self)
        person = session.query(Person).filter_by(Id=id).first()
        return person

    def get_persons(self, query=True):
        session = BaseRepository.get_session(self)
        persons = session.query(Person).filter(query).all()
        return list(persons)

