from api.repositories.person_repository import PersonRepository
from api.services.comparer_service import ComparerService
from api.services.dataset_service import DatasetService
from api.services.person_service import PersonService

import api.services.face_detector.factory as face_detector_factory
import api.services.face_comparer.factory as face_comparer_factory

class ServiceLocator:

    def __init__(self):
        self.person_repository = PersonRepository()
        self.dataset_service = DatasetService()
        self.person_service = PersonService(self.person_repository)
        self.face_comparer = face_comparer_factory.get_face_comparer('default')
        self.face_detector = face_detector_factory.get_face_detector('default')
        self.comparer_service = ComparerService(self.face_detector, self.face_comparer, self.dataset_service,
                                                self.person_service, True)

        self.face_detector.initialize()
        self.face_comparer.initialize(self.face_comparer.default_model_path, self.face_detector)
