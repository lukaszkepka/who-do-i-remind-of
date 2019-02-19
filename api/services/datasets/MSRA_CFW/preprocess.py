""" MSRA_CFW/preprocess

Script for preprocessing dataset before it can be used as database of images.
It deletes redundant images from person directory leaving only one representative image.
Image to be left is choosen randomly

"""
import PIL
import cv2
from scipy import misc
import time
from os import listdir
from os.path import isfile, join
import random
import argparse
import os

from PIL import Image


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


def capitalize_name(dir_full_path):
    dataset_path, dir = os.path.split(dir_full_path)

    name_parts = dir.split()
    capitalized_dir = " ".join([name_part.capitalize() for name_part in name_parts])

    capitalized_name = os.path.join(dataset_path, capitalized_dir)
    os.rename(dir_full_path, capitalized_name)


def remove_redundant_images(dir_full_path):
    files_other = []
    files_jpg = []

    for file in listdir(dir_full_path):
        filepath = join(dir_full_path, file)
        if isfile(filepath):
            if filepath.endswith('.jpg'):
                files_jpg.append(filepath)
            else:
                files_other.append(filepath)

    save_index = random.randint(0, len(files_jpg) - 1)
    for i, file in enumerate(files_jpg):
        if i != save_index:
            os.remove(file)

    for i, file in enumerate(files_other):
        os.remove(file)


def resize_image(dir_full_path):
    files = listdir(dir_full_path)
    if len(files) == 1:
        img_path = os.path.join(dir_full_path, files[0])
        # Load image to compare
        img = misc.imread(img_path, mode='RGB')
        img = cv2.resize(img.astype('uint8'), dsize=(640, 640))
        misc.imsave(img_path, img)


def log_progress(dir_full_path):
    print('Finished processing path = {0}'.format(dir_full_path))


def main():
    start = time.time()
    args = parse_arguments()

    for dir in list_dirs(args.dataset_path):
        dir_full_path = os.path.join(args.dataset_path, dir)

        capitalize_name(dir_full_path)
        remove_redundant_images(dir_full_path)
        resize_image(dir_full_path)
        log_progress(dir_full_path)

    stop = time.time()
    print("Processing {0} files took {1:.2f} s".format(len(list_dirs(args.dataset_path)), (stop - start)))


if __name__ == '__main__':
    main()
