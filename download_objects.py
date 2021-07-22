# -*- coding: utf-8 -*-

from __future__ import print_function, division
import argparse
from os.path import join

import subprocess
from urllib.request import Request, urlopen

__author__ = 'Fisher Yu'
__email__ = 'fy@cs.princeton.edu'
__license__ = 'MIT'


def download(out_dir, category):
    url = 'http://dl.yf.io/lsun/objects/{category}.zip'.format(**locals())
    print(url)
    out_name = '{category}.zip'.format(**locals())
    out_path = join(out_dir, out_name)
    cmd = ['curl', url, '-o', out_path]
    print('Downloading', category, 'set')
    subprocess.call(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out_dir', default='')
    args = parser.parse_args()

    categories = ['airplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'dining_table', 'dog', 'horse', 'motorbike', 'person', 'potted_plant', 'sheep', 'sofa', 'train' ,'tv-monitor']
    print('Downloading', len(categories), 'categories')
    for category in categories:
        download(args.out_dir, category)

if __name__ == '__main__':
    main()

