from unittest import TestCase
from Image import Image
from functions import *

SAMPLE_FILE = "/home/fargus/Pictures/HelpingRyan/1.png"


class TestImage(TestCase):
    def test_md5(self):
        i = Image(SAMPLE_FILE, [], calculate_md5=True)
        pass
        # assert i.md5 is not None


class TestConfig(TestCase):
    def test_load_config(self):
        load_config()

