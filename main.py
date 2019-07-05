from functions import *

"""

Sort Images

1. loads config ( creating all necessary directories )
2. gets all images from source directory
"""


# 1.
config = load_config()

# 2.
all_pictures = get_files(config)

print(all_pictures)