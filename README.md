# LSUN Scene Classification

## Data Release

All the images in one category are stored in one lmdb database file. The value
 of each entry is the jpg binary data. We resize all the images so that the
 smaller dimension is 256 and compress the images in jpeg with quality 75.

## Demo code

### Dependency

Install Python

Install Python dependency: numpy, lmdb, opencv

### Usage:

View the lmdb content

```bash
python2.7 data.py view <image db path>
```

Export the images to a folder

```bash
python2.7 data.py export <image db path> --out_dir <output directory>
```

### Example:

Export all the images in valuation sets in the current folder to a "data"
subfolder.

```bash
python2.7 data.py export *_val_lmdb --out_dir data
```