"""
Test Cases for random password generator
"""
import unittest
import sys
from easy_password_generator import PassGen

class TestRPG(unittest.TestCase):

    def test_generate_random(self):
        pg = PassGen()
        self.assertTrue(6 <= len(pg.generate()) <= 16)

    def test_generate_with_length(self):
        pg = PassGen()
        pg.minlen = 10
        pg.maxlen = 10
        self.assertEqual(len(pg.generate()), 10)


if __name__ == '__main__':
    unittest.main()