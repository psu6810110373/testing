import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from production.caesar import caesarCipher # อิมพอร์ต Production Code เข้ามา

class TestCaesarCipher(unittest.TestCase):

    def test_happy_path(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_wrap_around(self):
        self.assertEqual(caesarCipher("xyz", 3), "abc")
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_large_shift_factor(self):
        self.assertEqual(caesarCipher("abc", 28), "cde") # เลื่อน 28 มีค่าเท่ากับเลื่อน 2

    def test_special_characters_and_numbers(self):
        self.assertEqual(caesarCipher("Hello, World! 123", 5), "Mjqqt, Btwqi! 123")

if __name__ == '__main__':
    unittest.main()