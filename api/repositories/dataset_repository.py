from api.persistence.models.dataset import Dataset
from api.repositories.base_repository import BaseRepository


class DatasetRepository(BaseRepository):

    def add_dataset(self, dataset):
        if type(dataset) is not Dataset:
            return
        session = BaseRepository.get_session(self)
        session.add(dataset)
        session.commit()

    def update_dataset(self, updated_dataset):
        if type(updated_dataset) is not Dataset:
            return
        session = BaseRepository.get_session(self)
        dataset = session.query(Dataset).filter_by(Id=updated_dataset.Id).first()
        properties = dir(dataset)
        for prop in properties:
            if prop != 'Id' and not prop.startswith('_') and not prop.endswith('_'):
                setattr(dataset, prop, getattr(updated_dataset, prop))

        session.commit()

    def get_dataset(self, id):
        session = BaseRepository.get_session(self)
        dataset = session.query(Dataset).filter_by(Id=id).first()
        return dataset

    def get_datasets(self, query=True):
        session = BaseRepository.get_session(self)
        datasets = session.query(Dataset).filter(query).all()
        return list(datasets)

