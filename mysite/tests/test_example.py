import unittest

class TestAdd(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(2+2, 5)

if __name__ == '__main__':
    unittest.main()