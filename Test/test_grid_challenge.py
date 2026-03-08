import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from production.grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_yes_condition(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_no_condition(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        self.assertEqual(gridChallenge(grid), "NO")

    def test_single_element(self):
        grid = ['a']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_already_sorted(self):
        grid = ['abc', 'def', 'ghi']
        self.assertEqual(gridChallenge(grid), "YES")

if __name__ == '__main__':
    unittest.main()