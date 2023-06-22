import unittest
from ..images_compare.verify import verify_images


class TestVerifyImages(unittest.TestCase):
    def test_incorrect_file_path(self):
        self.assertRaises(FileNotFoundError, verify_images, "test_1.png", "test_2.png")

    def test_same_images(self):
        res = verify_images(
            "src/tests/test_img/test_1.png", "src/tests/test_img/test_1.png"
        )
        self.assertTrue(res)

    def test_similar_images_0_0001_threshold(self):
        res = verify_images(
            "src/tests/test_img/test_1.png", "src/tests/test_img/test_2.png"
        )
        self.assertFalse(res)

    def test_similar_images_0_1_threshold(self):
        res = verify_images(
            "src/tests/test_img/test_1.png", "src/tests/test_img/test_2.png", 0.1
        )
        self.assertTrue(res)

    def test_different_images(self):
        res = verify_images(
            "src/tests/test_img/test_1.png", "src/tests/test_img/test_3.png"
        )
        self.assertFalse(res)
