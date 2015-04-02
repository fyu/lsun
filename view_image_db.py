#!/usr/bin/python

from __future__ import print_function
import cv2
import lmdb
import numpy
import sys

__author__ = 'Fisher Yu'
__email__ = 'fy@cs.princeton.edu'


def view(db_path):
    window_name = 'LSUN'
    cv2.namedWindow(window_name)
    env = lmdb.open(db_path, map_size=1099511627776,
                    max_readers=10000, readonly=True)
    with env.begin(write=False) as txn:
        cursor = txn.cursor()
        for key, val in cursor:
            print(key)
            img = cv2.imdecode(
                numpy.array(bytearray(val), dtype=numpy.uint8),
                cv2.CV_LOAD_IMAGE_COLOR)
            cv2.imshow(window_name, img)
            c = cv2.waitKey()
            if c == 27:
                break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:', sys.argv[0], '<lmdb path>')
    view(sys.argv[1])
