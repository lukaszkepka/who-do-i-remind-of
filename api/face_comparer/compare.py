"""Performs face alignment and calculates L2 distance between the embeddings of images."""

# MIT License
# 
# Copyright (c) 2016 David Sandberg
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import argparse
import os
import copy

from scipy import misc
import api.face_detector.factory as face_detector_factory
import api.face_comparer.factory as face_comparer_factory


def main(args):
    # Initialization
    face_detector = face_detector_factory.get_face_detector('PRO')
    face_detector.initialize()

    face_comparer = face_comparer_factory.get_face_comparer('facenet')
    face_comparer.initialize(args.model, face_detector)

    # Read images
    tmp_image_paths = copy.copy(args.image_files)
    faces = []
    for image in tmp_image_paths:
        img = misc.imread(os.path.expanduser(image), mode='RGB')

        # Crop faces
        faces.append(face_detector.detect_face(img))

    distance_matrix = face_comparer.compare_with_images(faces[0], faces)
    print_matrix(distance_matrix)

    print('end')


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


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('model', type=str,
                        help='Could be either a directory containing the meta_file and ckpt_file or a model protobuf (.pb) file')
    parser.add_argument('image_files', type=str, nargs='+', help='Images to compare')
    parser.add_argument('--image_size', type=int,
                        help='Image size (height, width) in pixels.', default=160)
    parser.add_argument('--margin', type=int,
                        help='Margin for the crop around the bounding box (height, width) in pixels.', default=44)
    parser.add_argument('--gpu_memory_fraction', type=float,
                        help='Upper bound on the amount of GPU memory that will be used by the process.', default=1.0)
    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
