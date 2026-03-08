import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from production.funny import funnyString 

class TestFunnyString(unittest.TestCase):

    def test_is_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("lmnop"), "Funny") # ตัวอักษรเรียงกัน ระยะห่างเป็น 1 หมด

    def test_is_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_same_characters(self):
        self.assertEqual(funnyString("aaaa"), "Funny")
        
    def test_two_characters(self):
        self.assertEqual(funnyString("ab"), "Funny")

if __name__ == '__main__':
    unittest.main()