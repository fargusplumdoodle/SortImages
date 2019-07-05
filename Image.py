import os
import sys
import hashlib

#from PIL import image

class Image(object):
    def __init__(self, path, profiles, calculate_info=False):
        """

        :param path: path to image file
        :param profiles: from config
        :param calculate_info: if this object needs to calculate md5 and image info
        """

        # getting name info
        self.path = path
        self.extention = os.path.splitext(path)[1]
        self.name = os.path.splitext(path)[0].split('/')[-1]

        self.valid_profiles = profiles

        self.width, self.height, self.ratio = self.get_image_info()

        self.md5 = self.calculate_md5() if calculate_info else None

        print(self.md5)

    def calculate_md5(self):
        with open(self.path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def get_image_info(self):
        return 10, 1, 1

