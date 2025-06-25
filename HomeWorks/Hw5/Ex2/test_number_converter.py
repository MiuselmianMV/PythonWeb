import unittest
from .NumberConverter import NumberConverter


class TestNumberConverter(unittest.TestCase):
    def setUp(self):
        self.num = NumberConverter(42)

    def test_get_set_value(self):
        self.assertEqual(self.num.get_value(), 42)
        self.num.set_value(100)
        self.assertEqual(self.num.get_value(), 100)

    def test_to_binary(self):
        self.assertEqual(self.num.to_binary(), '0b101010')

    def test_to_octal(self):
        self.assertEqual(self.num.to_octal(), '0o52')

    def test_to_hex(self):
        self.assertEqual(self.num.to_hex(), '0x2a')


