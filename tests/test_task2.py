import unittest
from task_2.utils import *


class TestAggregatedThreatScore(unittest.TestCase):

    def test_balanced_data(self):
        departments = [
            {"scores": generate_random_data(40, 5, 50), "importance": 3},
            {"scores": generate_random_data(42, 5, 50), "importance": 3},
            {"scores": generate_random_data(38, 5, 50), "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(35 <= result <= 45, "Результат должен быть средним по уровням угроз")

    def test_one_high_risk_department(self):
        departments = [
            {"scores": generate_random_data(10, 5, 100), "importance": 3},
            {"scores": generate_random_data(90, 5, 50), "importance": 2},
            {"scores": generate_random_data(15, 5, 100), "importance": 3},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result > 70, "Результат должен учитывать высокий риск одного департамента")

    def test_high_risk_with_low_importance(self):
        departments = [
            {"scores": generate_random_data(10, 5, 100), "importance": 4},
            {"scores": generate_random_data(90, 5, 10), "importance": 1},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result > 60, "Даже департамент с низкой важностью должен поднимать результат")

    def test_all_high_risk(self):
        departments = [
            {"scores": generate_random_data(80, 5, 50), "importance": 3},
            {"scores": generate_random_data(85, 5, 50), "importance": 2},
        ]
        result = calculate_aggregated_threat_score(departments)
        self.assertTrue(result > 80, "Все департаменты с высоким риском должны давать высокий результат")



if __name__ == "__main__":
    unittest.main()