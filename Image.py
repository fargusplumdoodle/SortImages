import os
import hashlib

from PIL import Image as pilimage


class Image(object):
    def __init__(self, path, profiles, calculate_info=False):
        """
        :param path: path to image file
        :param profiles: from config
        :param calculate_info: if this object needs to calculate md5 and image info
        """
        self.failed = False
        self.reason = None

        # getting name info
        self.path = path
        self.profiles = profiles
        try:
            self.extention = os.path.splitext(path)[1]
            self.name = os.path.splitext(path)[0].split("/")[-1]
        except Exception:
            self.fail("error accessing file")
            return

        # getting md5 sum
        try:
            self.md5 = self.calculate_md5() if calculate_info else None
        except Exception:
            self.fail("unable to calculate md5")
            return

        # getting image info
        try:
            if calculate_info:
                self.width, self.height, self.ratio = self.get_image_info()
                self.valid_profiles = self.calculate_valid_profiles()
            else:
                self.width, self.height, self.ratio = None, None, None

        except Exception:
            self.fail("unable to get image info")
            return

    def calculate_valid_profiles(self):
        # checking if image is within parameters of each profile specified in the config file
        valid_profiles = []
        for profile in self.profiles:
            if (
                self.width >= self.profiles[profile]["min_width"]
                and self.height >= self.profiles[profile]["min_height"]
                and (
                    self.profiles[profile]["min_ratio"]
                    <= self.ratio
                    <= self.profiles[profile]["max_ratio"]
                )
            ):
                valid_profiles.append(profile)
        return valid_profiles

    def calculate_md5(self):
        with open(self.path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    def get_image_info(self):
        im = pilimage.open(self.path)

        width = int(im.size[0])
        height = int(im.size[1])
        ratio = float(width) / height

        return width, height, ratio

    def fail(self, reason):
        self.failed = True
        self.reason = reason + " " + str(self)

    def __str__(self):
        return self.path
