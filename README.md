# LSUN

Please check [LSUN webpage](http://www.yf.io/p/lsun) for more information about the dataset.

## Data Release

All the images in one category are stored in one lmdb database
file. The value
 of each entry is the jpg binary data. We resize all the images so
 that the
  smaller dimension is 256 and compress the images in jpeg with
  quality 75.
  
### Citing LSUN

If you find LSUN dataset useful in your research, please consider citing:

    @article{yu15lsun,
        Author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},
        Title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop},
        Journal = {arXiv preprint arXiv:1506.03365},
        Year = {2015}
    }

### Download data
Please make sure you have cURL installed
```bash
# Download the whole latest data set
python3 download.py
# Download the whole latest data set to <data_dir>
python3 download.py -o <data_dir>
# Download data for bedroom
python3 download.py -c bedroom
# Download testing set
python3 download.py -c test
```

## Demo code

### Dependency

Install Python

Install Python dependency: numpy, lmdb, opencv

### Usage:

View the lmdb content

```bash
python3 data.py view <image db path>
```

Export the images to a folder

```bash
python3 data.py export <image db path> --out_dir <output directory>
```

### Example:

Export all the images in valuation sets in the current folder to a
"data"
subfolder.

```bash
python3 data.py export *_val_lmdb --out_dir data
```

## Submission

We expect one category prediction for each image in the testing
set. The name of each image is the key value in the LMDB
database. Each category has an index as listed in
[index list](https://github.com/fyu/lsun_toolkit/blob/master/category_indices.txt). The
submitted results on the testing set will be stored in a text file
with one line per image. In each line, there are two fields separated
by a whitespace. The first is the image key and the second is the
predicted category index. For example:

```
0001c44e5f5175a7e6358d207660f971d90abaf4 0
000319b73404935eec40ac49d1865ce197b3a553 1
00038e8b13a97577ada8a884702d607220ce6d15 2
00039ba1bf659c30e50b757280efd5eba6fc2fe1 3
...
```

The score for the submission is the percentage of correctly predicted
labels. In our evaluation, we will double check our ground truth
labels for the testing images and we may remove some images with
controversial labels in the final evaluation.
