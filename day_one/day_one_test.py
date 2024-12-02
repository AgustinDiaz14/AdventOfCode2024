import unittest

from day_one import calculate_distances, calculate_occurrences


class DayOne(unittest.TestCase):
    def test_calculate_distances(self):
        result = calculate_distances("./inputs/test_input.txt")
        self.assertEqual(result, 11)  # add assertion here

    def test_calculate_occurrences(self):
        result = calculate_occurrences("./inputs/test_input.txt")
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()
