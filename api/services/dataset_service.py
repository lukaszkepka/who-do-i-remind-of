import numpy as np

from api.repositories.person_repository import PersonRepository
from api.services.comparer_service import FeatureMatrix


class DatasetService:

    def __init__(self):
        self.person_repository = PersonRepository()

    def get_feature_matrix(self, dataset_id):
        people_from_dataset = self.person_repository.get_persons(dataset_id)

        feature_matrix = FeatureMatrix(len(people_from_dataset))

        for i, person in enumerate(people_from_dataset):
            features = np.frombuffer(person.model, dtype=np.float32)
            feature_matrix.add_feature_vector(i, person.id, features)

        return feature_matrix
