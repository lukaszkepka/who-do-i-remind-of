import numpy as np
from scipy import misc
import api.services.datasets.MSRA_CFW.dataset_creator as dataset
from api.dto.comparison_dto import ComparisonDTO
from api.services.face_comparer.utils import print_results
import base64

class FeatureMatrix:

    def __init__(self, count):
        self.index_id_map = {}
        self.features = np.zeros((count, 512))

        for i in range(count):
            self.index_id_map[i] = -1

    def add_feature_vector(self, index, person_id, features):
        self.index_id_map[index] = person_id
        self.features[index, :] = features

    def get_features(self, index):
        return self.index_id_map[index], self.features[index, :]


class ComparerService:

    def __init__(self, face_detector, face_comparer, dataset_service, person_service, display_result=False):
        self.display_result = display_result
        self.dataset_service = dataset_service
        self.person_service = person_service
        self.face_detector = face_detector
        self.face_comparer = face_comparer

    def compare(self, dataset_id, photo, take=10):
        cropped_face = self.face_detector.detect_face(photo)
        feature_matrix = self.dataset_service.get_feature_matrix(dataset_id)

        distance_matrix = self.face_comparer.compare_with_features(cropped_face, feature_matrix.features)

        # Get indexes of <take> best results
        indexes = np.argsort(distance_matrix[0, :])[:take]

        # Create comparison objects
        comparison_results = self.create_comparing_result(feature_matrix, distance_matrix, indexes)

        if self.display_result:
            self.print_results(comparison_results)

        return comparison_results

    def create_comparing_result(self, feature_matrix, distance_matrix, indexes):
        comparing_results = []
        for index in indexes:
            person_id, features = feature_matrix.get_features(index)

            try:
                person = self.person_service.get_person(person_id)
                with open(person.photo_uri, "rb") as imageFile:
                    file_content = imageFile.read()
                    image_base64 = base64.encodebytes(file_content).decode("utf-8")

                comparing_results.append(
                    ComparisonDTO(person_id, person.name, image_base64, distance_matrix[0, index]))
            except Exception as ex:
                print(ex)
        return comparing_results

    @staticmethod
    def print_results(results):
        faces = [result.image for result in results]
        distances = [result.similarity_ratio for result in results]
        names = [result.name for result in results]
        indexes = range(len(results))
        print_results(faces, distances, names, indexes)
