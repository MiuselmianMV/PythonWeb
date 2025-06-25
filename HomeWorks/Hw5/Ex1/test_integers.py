import unittest
from .Integers import IntegerSet


class TestIntegers(unittest.TestCase):
    def setUp(self):
        self.numSet = IntegerSet([1, 2, 3, 4, 5])

    def test_get_sum(self):
        self.assertEqual(self.numSet.get_sum(), 15)

    def test_get_average(self):
        self.assertEqual(self.numSet.get_average(), 3)

    def test_get_max(self):
        self.assertEqual(self.numSet.get_max(), 5)

    def test_get_min(self):
        self.assertEqual(self.numSet.get_min(), 1)

