import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from production.two_characters import alternate

class TestTwoCharacters(unittest.TestCase):

    def test_happy_path(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_no_valid_alternating_string(self):
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("a"), 0) 

    def test_already_two_alternating_characters(self):
        self.assertEqual(alternate("aba"), 3)
        self.assertEqual(alternate("abab"), 4)

    def test_complex_string(self):
        self.assertEqual(alternate("asdcbsdcagfsdbgdfanfghbsfdab"), 8)

if __name__ == '__main__':
    unittest.main()