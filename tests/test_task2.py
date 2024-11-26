import unittest
from task_2.utils import *


class TestAggregatedThreatScore(unittest.TestCase):

    def test_balanced_data(self):
        departments = [
            {"scores": [40] * 50, "importance": 3},
            {"scores": [50] * 50, "importance": 3},
            {"scores": [45] * 50, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertEqual(result, 45, "Средние значения должны возвращать средний результат")

    def test_one_bad_department(self):
        departments = [
            {"scores": [10] * 50, "importance": 3},
            {"scores": [90] * 50, "importance": 3},
            {"scores": [20] * 50, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result > 60, "Результат должен учитывать высокий риск в одном департаменте")

    def test_small_bad_department(self):
        departments = [
            {"scores": [20] * 100, "importance": 5},
            {"scores": [90] * 10, "importance": 1},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result > 50, "Даже маленький департамент с угрозой должен влиять")

    def test_all_good_one_bad(self):
        departments = [
            {"scores": [10] * 100, "importance": 3},
            {"scores": [80] * 10, "importance": 5},
            {"scores": [10] * 100, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result > 60, "Результат должен отражать риск от плохого департамента")

    def test_all_good(self):
        departments = [
            {"scores": [10] * 50, "importance": 3},
            {"scores": [15] * 50, "importance": 3},
            {"scores": [20] * 50, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result < 20, "Все хорошие департаменты должны давать низкий результат")

    def test_extreme_values(self):
        departments = [
            {"scores": [0] * 50, "importance": 3},
            {"scores": [90] * 50, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(40 <= result <= 60, "Результат должен быть между крайними значениями")

    def test_no_penalty(self):
        departments = [
            {"scores": [50] * 50, "importance": 2},
            {"scores": [60] * 50, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments, penalty_weight=0)
        self.assertEqual(result, 55, "Если штрафы не применяются, результат должен быть средней угрозой")

    def test_empty_departments(self):
        departments = []
        with self.assertRaises(ZeroDivisionError):
            calculate_aggregated_threat_score(departments)

    def test_valid_result_range(self):
        departments = [
            {"scores": [50] * 50, "importance": 2},
            {"scores": [90] * 50, "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(0 <= result <= 90, "Результат должен быть в диапазоне 0-90")


if __name__ == "__main__":
    unittest.main()

