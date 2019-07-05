from unittest import TestCase
from Image import Image
from functions import *
import shutil

SAMPLE_FILE = "/home/fargus/Pictures/"


class TestImage(TestCase):
    def test_md5(self):
        i = Image(SAMPLE_FILE, [], calculate_info=True)


class TestSortImages(TestCase):
    def setUp(self) -> None:
        pass

    def test_load_config(self):
        shutil.rmtree("/tmp/SortWallpaper")
        load_config()


