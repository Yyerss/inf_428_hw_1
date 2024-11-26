import unittest
from task_3.utils import *


class TestCyclicTimeDifferenceTrig(unittest.TestCase):

    def test_same_time(self):
        result = cyclic_time_difference_trig(5, 5)
        self.assertEqual(result, 0, "Если время одинаковое, разница должна быть 0")

    def test_no_wraparound(self):
        result = cyclic_time_difference_trig(5, 8)
        self.assertEqual(result, 3, "Разница между 5 и 8 должна быть 3")

    def test_wraparound(self):
        result = cyclic_time_difference_trig(23, 1)
        self.assertEqual(result, 2, "Разница между 23:00 и 01:00 должна быть 2")

    def test_reverse_wraparound(self):
        result = cyclic_time_difference_trig(1, 23)
        self.assertEqual(result, 2, "Разница между 01:00 и 23:00 должна быть 2")

    def test_midnight_difference(self):
        result = cyclic_time_difference_trig(0, 12)
        self.assertEqual(result, 12, "Разница между 00:00 и 12:00 должна быть 12")

    def test_large_to_small(self):
        result = cyclic_time_difference_trig(20, 4)
        self.assertEqual(result, 8, "Разница между 20:00 и 04:00 должна быть 8")

    def test_small_to_large(self):
        result = cyclic_time_difference_trig(4, 20)
        self.assertEqual(result, 8, "Разница между 04:00 и 20:00 должна быть 8")

    def test_invalid_time1(self):
        with self.assertRaises(ValueError):
            cyclic_time_difference_trig(-1, 5)

    def test_invalid_time2(self):
        with self.assertRaises(ValueError):
            cyclic_time_difference_trig(5, 25)

if __name__ == '__main__':
    unittest.main()
