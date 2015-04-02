# lsun_toolkit

## Data Release v0 (2015-04-01)

All the images in one category are stored in one lmdb database file. The value
 of each entry is the jpg binary data. We resize all the images to 256 x 256.

## Demo code

You need first install python

Python dependency: numpy, lmdb, opencv

Usage:

python view_image_db.py <image db path>
