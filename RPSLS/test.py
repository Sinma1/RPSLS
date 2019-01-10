import os
import unittest

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    loader = unittest.TestLoader()

    runner = unittest.TextTestRunner()
    runner.run(loader.discover(f"{dir_path}/tests"))
