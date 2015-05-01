# LSUN Scene Classification

## Data Release

All the images in one category are stored in one lmdb database file. The value
 of each entry is the jpg binary data. We resize all the images so that the 
 smaller dimension is 256 and compress the images in jpeg with quality 75.

## Demo code

Install Python

Install Python dependency: numpy, lmdb, opencv

Usage:

<pre><code>python view_image_db.py &lt;image db path&gt; </code></pre>
