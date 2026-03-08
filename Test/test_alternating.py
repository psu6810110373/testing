import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from production.alternating import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_all_same_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_already_alternating(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)

    def test_mixed_characters(self): 
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
        self.assertEqual(alternatingCharacters("AABBAABB"), 4) # เหลือ ABAB

    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)

if __name__ == '__main__':
    unittest.main()