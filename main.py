#!/usr/bin/python3
from functions import *

"""
Sort Images

1. loads config ( creating all necessary directories )
2. gets all images from source directory
3. copies the images into their valid profile directories in dest, with the name being the md5 sum
4. print any errors that occurred
"""


# 1.
config = load_config()

print(
    """
==== START ====
SRC: %s
DEST: %s
"""
    % (config["src"], config["dest"])
)

# 2.
new_images, failed_images = get_files(config)

# 3.
failed_images = failed_images + copy_images(new_images, config)

# 4.
if config["verbose"]:
    for x in failed_images:
        print("error: ", x.path)

print(
    """
---- COMPLETE ----
Processed: %s images
Errors: %s
================
"""
    % (len(new_images), len(failed_images))
)
