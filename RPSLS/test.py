import os
import unittest

if __name__ == '__main__':
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    LOADER = unittest.TestLoader()

    RUNNER = unittest.TextTestRunner()
    RUNNER.run(LOADER.discover(f"{DIR_PATH}/tests"))
