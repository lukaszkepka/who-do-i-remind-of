from api.repositories.person_repository import PersonRepository
from api.services.comparer_service import ComparerService
from api.services.dataset_service import DatasetService
from api.services.person_service import PersonService

import api.services.face_detector.factory as face_detector_factory
import api.services.face_comparer.factory as face_comparer_factory


class ServiceLocator:

    def __init__(self):
        person_repository = PersonRepository()

        person_repository = person_repository
        dataset_service = DatasetService()
        person_service = PersonService(person_repository)
        face_comparer = face_comparer_factory.get_face_comparer('default')
        face_detector = face_detector_factory.get_face_detector('default')
        comparer_service = ComparerService(face_detector, face_comparer, dataset_service,
                                           person_service)

        face_detector.initialize()
        face_comparer.initialize(face_comparer.default_model_path, face_detector)

        self.person_repository = person_repository
        self.dataset_service = dataset_service
        self.person_service = person_service
        self.face_comparer = face_comparer
        self.face_detector = face_detector
        self.comparer_service = comparer_service
