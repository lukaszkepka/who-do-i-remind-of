"""Functions for building the face recognition network.
"""
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

# pylint: disable=missing-docstring
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import math
import random
import re
import os
import copy

from scipy import misc
from tensorflow.python.platform import gfile

# 1: Random rotate 2: Random crop  4: Random flip  8:  Fixed image standardization  16: Flip
RANDOM_ROTATE = 1
RANDOM_CROP = 2
RANDOM_FLIP = 4
FIXED_STANDARDIZATION = 8
FLIP = 16


class FaceComparer:

    def __init__(self):
        self.initialized = False
        self.face_detector = None
        self.model_path = ''

        self.graph = tf.Graph()
        self.session = tf.Session(graph=self.graph)
        self.embeddings = None
        self.images_placeholder = None
        self.phase_train_placeholder = None

    def initialize(self, model_path, face_detector):
        self.model_path = model_path
        self.face_detector = face_detector

        with self.graph.as_default() as graph:
            # Load the model
            load_model(self.model_path, self.session)

            self.images_placeholder = graph.get_tensor_by_name("input:0")
            self.embeddings = graph.get_tensor_by_name("embeddings:0")
            self.phase_train_placeholder = graph.get_tensor_by_name("phase_train:0")
        self.initialized = True

    def extract_features(self, images):
        feed_dict = {self.images_placeholder: images, self.phase_train_placeholder: False}
        emb = self.session.run(self.embeddings, feed_dict=feed_dict)
        return emb

    def compare_with_images(self, image, images):
        image_array = np.insert(images, 0, np.expand_dims(image, axis=0), axis=0)

        features = self.extract_features(image_array)

        query_features = np.expand_dims(features[0], axis=0)
        gallery_features = features[1:]
        distance_matrix = self.get_distance(query_features, gallery_features)

        return distance_matrix

    def compare_with_features(self, image, gallery_features):
        image_array = np.expand_dims(image, axis=0)
        query_features = self.extract_features(image_array)
        distance_matrix = self.get_distance(query_features, gallery_features)
        return distance_matrix

    def get_distance(self, features1, features2):
        distance_matrix = np.zeros((len(features1), len(features2)))

        for i in range(len(features1)):
            values = np.expand_dims(features1[i], axis=0)
            values = np.tile(values, (features2.shape[0], 1))
            distance_matrix[i, :] = np.sqrt(np.sum(np.square(np.subtract(values, features2)), axis=1))
        return distance_matrix


class ImageClass():
    "Stores the paths to images for a given class"

    def __init__(self, name, image_paths):
        self.name = name
        self.image_paths = image_paths

    def __str__(self):
        return self.name + ', ' + str(len(self.image_paths)) + ' images'

    def __len__(self):
        return len(self.image_paths)


def load_model(model, session, input_map=None):
    # Check if the model is a model directory (containing a metagraph and a checkpoint file)
    # or if it is a protobuf file with a frozen graph
    model_exp = os.path.expanduser(model)
    if os.path.isfile(model_exp):
        print('Model filename: %s' % model_exp)
        with gfile.FastGFile(model_exp, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, input_map=input_map, name='')
    else:
        print('Model directory: %s' % model_exp)
        meta_file, ckpt_file = get_model_filenames(model_exp)

        print('Metagraph file: %s' % meta_file)
        print('Checkpoint file: %s' % ckpt_file)

        saver = tf.train.import_meta_graph(os.path.join(model_exp, meta_file), input_map=input_map)
        saver.restore(session, os.path.join(model_exp, ckpt_file))


def get_model_filenames(model_dir):
    files = os.listdir(model_dir)
    meta_files = [s for s in files if s.endswith('.meta')]
    if len(meta_files) == 0:
        raise ValueError('No meta file found in the model directory (%s)' % model_dir)
    elif len(meta_files) > 1:
        raise ValueError('There should not be more than one meta file in the model directory (%s)' % model_dir)
    meta_file = meta_files[0]
    ckpt = tf.train.get_checkpoint_state(model_dir)
    if ckpt and ckpt.model_checkpoint_path:
        ckpt_file = os.path.basename(ckpt.model_checkpoint_path)
        return meta_file, ckpt_file

    meta_files = [s for s in files if '.ckpt' in s]
    max_step = -1
    for f in files:
        step_str = re.match(r'(^model-[\w\- ]+.ckpt-(\d+))', f)
        if step_str is not None and len(step_str.groups()) >= 2:
            step = int(step_str.groups()[1])
            if step > max_step:
                max_step = step
                ckpt_file = step_str.groups()[0]
    return meta_file, ckpt_file
