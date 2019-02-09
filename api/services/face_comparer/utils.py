import math
from scipy import misc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


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


def print_results(faces, distances, names, indexes, shapes):
    columns = 5
    rows = math.ceil(len(faces) / columns)
    f, axarr = plt.subplots(rows, columns)

    for i in range(len(faces)):
        index = indexes[i]
        xi = math.floor(i / columns)
        yi = i % columns

        face = np.frombuffer(faces[index], dtype=np.uint8)
        face = face.reshape(shapes[index])
        resized_img = misc.imresize(face, (300, 300), interp='bilinear')

        axarr[xi, yi].imshow(resized_img)
        axarr[xi, yi].set_title('{0}\n({1:.2f})'.format(names[index], distances[index]))

    for i in range(rows):
        for j in range(columns):
            axarr[i, j].axis('off')

    plt.savefig('image_comparison_set.png')


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
