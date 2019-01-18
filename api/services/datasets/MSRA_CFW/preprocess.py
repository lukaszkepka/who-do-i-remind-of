""" MSRA_CFW/preprocess

Script for preprocessing dataset before it can be used as database of images.
It deletes redundant images from person directory leaving only one representative image.
Image to be left is choosen randomly

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