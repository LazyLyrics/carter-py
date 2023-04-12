# run_tests.py

import unittest

if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
