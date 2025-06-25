import unittest

from Ex1 import *
from Ex2 import *


def main():
    loader = unittest.TestLoader()
    test1 = loader.loadTestsFromTestCase(TestIntegers)
    test2 = loader.loadTestsFromTestCase(TestNumberConverter)

    suite = unittest.TestSuite()
    suite.addTests(test1)
    suite.addTests(test2)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    main()
