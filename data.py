#!/usr/bin/env python2.7

from __future__ import print_function
import argparse
import cv2
import lmdb
import numpy
import os
from os.path import exists, join

__author__ = 'Fisher Yu'
__email__ = 'fy@cs.princeton.edu'
__license__ = 'MIT'


def view(db_path):
    window_name = 'LSUN'
    cv2.namedWindow(window_name)
    env = lmdb.open(db_path, map_size=1099511627776,
                    max_readers=100, readonly=True)
    with env.begin(write=False) as txn:
        cursor = txn.cursor()
        for key, val in cursor:
            print(key)
            print('Press ESC to exist or SPACE to advance.')
            img = cv2.imdecode(
                numpy.fromstring(val, dtype=numpy.uint8),
                cv2.CV_LOAD_IMAGE_COLOR)
            cv2.imshow(window_name, img)
            c = cv2.waitKey()
            if c == 27:
                break


def export_images(db_path, out_dir):
    env = lmdb.open(db_path, map_size=1099511627776,
                    max_readers=100, readonly=True)
    with env.begin(write=False) as txn:
        cursor = txn.cursor()
        for key, val in cursor:
            image_out_dir = join(out_dir, '/'.join(key[:6]))
            if not exists(image_out_dir):
                os.makedirs(image_out_dir)
            image_out_path = join(image_out_dir, key + '.jpg')
            with open(image_out_path, 'w') as fp:
                fp.write(val)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', nargs=1, type=str,
                        choices=['view', 'export'])
    parser.add_argument('lmdb_path', nargs=1, type=str)
    parser.add_argument('--out_dir', type=str, default='')
    args = parser.parse_args()

    command = args.command[0]
    lmdb_path = args.lmdb_path[0]

    if command == 'view':
        view(lmdb_path)
    elif command == 'export':
        export_images(lmdb_path, args.out_dir)


if __name__ == '__main__':
    main()