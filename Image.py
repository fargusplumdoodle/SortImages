import sys
import hashlib


class Image(object):
    def __init__(self, path, valid_profiles, calculate_md5=false):
        self.valid_profiles = valid_profiles

        self.width, self.height, self.ratio = self.get_image_info()

        if calculate_md5:
            self.md5 = self.calculate_md5()

    def calculate_md5(self):
        return "eyy"

    def get_image_info(self):
        return 10, 1, 1
