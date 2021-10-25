import unittest
from my_sum import sum
class TestSum(unittest.TestCase):
    def test_list_int(self):
        d = [5, 7, 9]
        result = sum(d)
        self.assertEqual(result, 21)

if __name__ == '__main__':
    unittest.main()
