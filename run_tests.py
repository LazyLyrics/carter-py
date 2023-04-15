# run_tests.py

import unittest
import asynctest

if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('tests', pattern='test_*.py')
    print(f"Running {test_suite.countTestCases()} synchronous tests")
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

    async_test_suite = asynctest.TestLoader().discover(
        'tests', pattern='async_test_*.py')
    print(f"Running {async_test_suite.countTestCases()} asynchronous tests")
    async_test_runner = asynctest.TextTestRunner()
    async_test_runner.run(async_test_suite)
