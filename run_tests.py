import unittest

if __name__ == "__main__":
    test_suite = unittest.defaultTestLoader.discover("carter-py", pattern="tests.py")
    unittest.TextTestRunner().run(test_suite)
