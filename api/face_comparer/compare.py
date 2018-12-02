import argparse
import os
import random
from urllib.request import urlopen
import numpy as np
import math
import cv2
from scipy import misc
import matplotlib.pyplot as plt
import api.datasets.MSRA_CFW.dataset_creator as dataset
import api.face_detector.factory as face_detector_factory
import api.face_comparer.factory as face_comparer_factory


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('dataset_path', type=str)
    parser.add_argument('image_path', type=str)
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Load image to compare
    with urlopen(args.image_path) as file:
        img = misc.imread(file, mode='RGB')

    plt.imshow(np.uint8(img))
    plt.title('Query image')
    plt.show()

    # Initialization
    face_detector = face_detector_factory.get_face_detector('default')
    face_detector.initialize()

    face_comparer = face_comparer_factory.get_face_comparer('default')
    face_comparer.initialize(face_comparer.default_model_path, face_detector)

    faces = []
    names = []
    images_num = 10
    feature_matrix = np.zeros((images_num, 512))
    for i, ret in enumerate(dataset.extract(args.dataset_path, face_detector, face_comparer, take=images_num)):
        names.append(ret[0])
        faces.append(ret[1])
        feature_matrix[i, :] = ret[2]

    cropped_face = face_detector.detect_face(img)
    distance_matrix = face_comparer.compare_with_features(cropped_face, feature_matrix)

    indexes = np.argsort(distance_matrix[0, :])
    print_results(faces, distance_matrix, indexes)

    cv2.waitKey(0)


def print_results(faces, distances, indexes):
    columns = 5
    rows = math.ceil(len(faces) / columns)
    f, axarr = plt.subplots(rows, columns)

    for i in range(len(faces)):
        index = indexes[i]
        xi = math.floor(i / columns)
        yi = i % columns

        resized_img = misc.imresize(faces[index], (300, 300), interp='bilinear')

        axarr[xi, yi].imshow(resized_img)
        axarr[xi, yi].set_title("{:0.2f}".format(distances[0, index]))

    for i in range(rows):
        for j in range(columns):
            axarr[i, j].axis('off')

    plt.show()


def print_matrix(distance_matrix):
    # Print distance matrix
    print('Distance matrix')
    print('    ', end='')
    for i in range(distance_matrix.shape[1]):
        print('    %1d     ' % i, end='')
    print('')
    for i in range(distance_matrix.shape[0]):
        print('%1d  ' % i, end='')
        for j in range(distance_matrix.shape[1]):
            dist = distance_matrix[i, j]
            print('  %1.4f  ' % dist, end='')
        print('')
    pass


if __name__ == '__main__':
    main()
