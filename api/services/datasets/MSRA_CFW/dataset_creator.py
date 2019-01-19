""" MSRA_CFW/dataset_creator

Script for iterating through image dataset and save person metadata to database
arguments :

- dataset_path - path to dataset to iterate

"""
import time
from os.path import isfile, join
from os import listdir
import argparse
import os
import numpy as np
from scipy import misc
import api.services.face_detector.factory as face_detector_factory
import api.services.face_comparer.factory as face_comparer_factory
from api.services.datasets.exceptions import ImageError, FaceNotFoundError
from api.services.domain_models.person_dm import PersonDomainModel


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-dataset_path', type=str)
    return parser.parse_args()


def list_dirs(path):
    dirs = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            dirs.append(full_path)
    return dirs


def extract_name(person_path):
    person_name = os.path.split(person_path)[-1]
    return person_name


def extract_cropped_image(person_image_path, face_detector):
    face_img = misc.imread(os.path.expanduser(person_image_path), mode='RGB')
    cropped_face = face_detector.detect_face(face_img)
    return cropped_face


def extract_features(person_image, face_comparer):
    person_image = np.expand_dims(np.asarray(person_image), axis=0)
    return face_comparer.extract_features(person_image)


def extract_person_model(person_path, face_detector, face_comparer):
    files = []
    for file in listdir(person_path):
        filepath = join(person_path, file)
        if isfile(filepath):
            if filepath.endswith('.jpg'):
                files.append(filepath)

    if len(files) == 0:
        raise ImageError("Error - Path contains no images")

    if len(files) > 1:
        raise ImageError("Error - Path contains more than one image")

    image_path = files[0]
    name = extract_name(person_path)
    cropped_face_image = extract_cropped_image(image_path, face_detector)
    features = extract_features(cropped_face_image, face_comparer)

    # TODO : Update according to new version of PersonDomainModel
    person_model = PersonDomainModel()
    person_model.name = name
    person_model.model = features.tobytes()
    person_model.photo_uri = image_path
    return person_model


def extract(dataset_path, face_detector, face_comparer, take=None):
    invalid_number_of_images = []
    images_without_face = []

    person_paths = list_dirs(dataset_path)

    if take is None:
        take = len(person_paths)

    start = time.time()
    for i, person_path in enumerate(person_paths[:take]):
        print("Processing {0} ({1}/{2})".format(person_path, i, len(person_paths)))

        try:
            yield extract_person_model(person_path, face_detector, face_comparer)
        except FaceNotFoundError as ex:
            images_without_face.append(person_path)
            print(ex)
        except ImageError as ex:
            invalid_number_of_images.append(person_path)
            print(ex)
        except Exception as ex:
            print('Unknown error - {0}'.format(ex))

    stop = time.time()
    print("Processing {0} files took {1:.2f} s".format(len(person_paths), (stop - start)))

    generate_report(invalid_number_of_images, images_without_face)


def generate_report(invalid_number_of_images, images_without_face):
    report = open("report.txt", "w+")

    report.write("Folders with invalid number of images :\n")
    for i in invalid_number_of_images:
        report.write(i + '\n')

    report.write("Folders with image that doesn't contain face :\n")
    for i in images_without_face:
        report.write(i + '\n')

    report.close()


def main():
    args = parse_arguments()

    # Initialization
    face_detector = face_detector_factory.get_face_detector('default')
    face_detector.initialize()

    face_comparer = face_comparer_factory.get_face_comparer('default')
    face_comparer.initialize(face_comparer.default_model_path, face_detector)

    # Run
    # TODO : Create dataset and add to database. All required fields provide from args
    for person_model in extract(args.dataset_path, face_detector, face_comparer):
        pass
        # TODO : Add person_model to database


if __name__ == '__main__':
    main()
