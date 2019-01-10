""" MSRA_CFW/dataset_loader

Script for iterating through image dataset and save person metadata to database
arguments :

- dataset_path - path to dataset to iterate

"""

import argparse
import os
import random
import numpy as np
from scipy import misc
import api.services.face_detector.factory as face_detector_factory
import api.services.face_comparer.factory as face_comparer_factory


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('dataset_path', type=str)
    return parser.parse_args(argv)


def list_dirs(path):
    dirs = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            dirs.append(full_path)
    return dirs


def extract_name(person_path):
    person_name = os.path.split(person_path)[-1]
    return person_name.capitalize()


def extract_cropped_image(person_path, face_detector):
    image_paths = []
    for item in os.listdir(person_path):
        full_path = os.path.join(person_path, item)
        if os.path.isfile(full_path):
            image_paths.append(full_path)

    image_index = random.randint(0, len(image_paths) - 1)
    image_path = image_paths[image_index]
    face_img = misc.imread(os.path.expanduser(image_path), mode='RGB')
    cropped_face = face_detector.detect_face(face_img)
    return cropped_face


def extract_features(person_image, face_comparer):
    person_image = np.expand_dims(np.asarray(person_image), axis=0)
    return face_comparer.extract_features(person_image)


def extract_person_model(person_path, face_detector, face_comparer):
    name = extract_name(person_path)
    cropped_face_image = extract_cropped_image(person_path, face_detector)
    features = extract_features(cropped_face_image, face_comparer)

    return name, cropped_face_image, features


def extract(dataset_path, face_detector, face_comparer, take=None):
    person_paths = list_dirs(dataset_path)

    if take is None:
        take = len(person_paths)

    for person_path in person_paths[:take]:
        name, cropped_face_image, features = extract_person_model(person_path, face_detector, face_comparer)
        yield name, cropped_face_image, features, person_path


def main():
    args = parse_arguments()

    # Initialization
    face_detector = face_detector_factory.get_face_detector('default')
    face_detector.initialize()

    face_comparer = face_comparer_factory.get_face_comparer('default')
    face_comparer.initialize(face_comparer.default_model_path, face_detector)

    pass


if __name__ == '__main__':
    main()
