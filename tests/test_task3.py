import unittest
from task_3.utils import time_difference


class TestTimeDifference(unittest.TestCase):

    def test_same_time(self):
        self.assertEqual(time_difference(5, 5), 0)

    def test_midnight_crossing(self):
        self.assertEqual(time_difference(23, 1), 2)
        self.assertEqual(time_difference(1, 23), 2)

    def test_within_same_day(self):
        self.assertEqual(time_difference(10, 14), 4)
        self.assertEqual(time_difference(14, 10), 4)

    def test_half_day_difference(self):
        self.assertEqual(time_difference(0, 12), 12)
        self.assertEqual(time_difference(6, 18), 12)


if __name__ == '__main__':
    unittest.main()
