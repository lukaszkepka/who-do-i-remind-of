import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

import argparse
import api.services.face_comparer.factory as face_comparer_factory
import api.services.face_detector.factory as face_detector_factory
from api.persistence.database_init import DatabaseConfig
from api.repositories.person_repository import PersonRepository
from api.services.comparer_service import ComparerService
from api.services.dataset_service import DatasetService
from api.services.person_service import PersonService


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-image_path', type=str)
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Load image to compare
    img = misc.imread(args.image_path, mode='RGB')

    plt.imshow(np.uint8(img))
    plt.title('Query image')
    plt.show()

    # Initialization
    face_detector = face_detector_factory.get_face_detector('default')
    face_detector.initialize()

    face_comparer = face_comparer_factory.get_face_comparer('default')
    face_comparer.initialize(face_comparer.default_model_path, face_detector)

    DatabaseConfig.config()
    dataset_service = DatasetService()
    person_repository = PersonRepository()
    person_service = PersonService(person_repository)

    comparer_service = ComparerService(face_detector, face_comparer, dataset_service, person_service, display_result=True)
    comparer_service.compare(1, img)


if __name__ == '__main__':
    main()
