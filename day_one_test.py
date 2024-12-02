import unittest

from day_one import calculate_distances


class DayOne(unittest.TestCase):
    def test_calculate_distances(self):
        result = calculate_distances("./inputs/day_one/test_input.txt")
        self.assertEqual(result, 11)  # add assertion here


if __name__ == '__main__':
    unittest.main()
