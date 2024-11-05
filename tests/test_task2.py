import unittest
from task_2.utils import generate_random_data, calculate_aggregated_threat_score


class TestAggregatedThreatScore(unittest.TestCase):

    def test_zero_threat(self):
        departments = [
            {"name": "Engineering", "importance": 3, "scores": [0] * 100},
            {"name": "Marketing", "importance": 2, "scores": [0] * 100},
            {"name": "Finance", "importance": 5, "scores": [0] * 100},
            {"name": "HR", "importance": 4, "scores": [0] * 100},
            {"name": "Science", "importance": 1, "scores": [0] * 100}
        ]
        score = calculate_aggregated_threat_score(departments)
        self.assertEqual(score, 0)

    def test_max_threat(self):
        departments = [
            {"name": "Engineering", "importance": 3, "scores": [90] * 100},
            {"name": "Marketing", "importance": 2, "scores": [90] * 100},
            {"name": "Finance", "importance": 5, "scores": [90] * 100},
            {"name": "HR", "importance": 4, "scores": [90] * 100},
            {"name": "Science", "importance": 1, "scores": [90] * 100}
        ]
        score = calculate_aggregated_threat_score(departments)
        self.assertEqual(score, 90)

    def test_mixed_threat_and_importance(self):
        departments = [
            {"name": "Engineering", "importance": 1, "scores": generate_random_data(10, 5, 100)},
            {"name": "Marketing", "importance": 2, "scores": generate_random_data(20, 5, 100)},
            {"name": "Finance", "importance": 3, "scores": generate_random_data(30, 5, 100)},
            {"name": "HR", "importance": 4, "scores": generate_random_data(40, 5, 100)},
            {"name": "Science", "importance": 5, "scores": generate_random_data(50, 5, 100)}
        ]
        score = calculate_aggregated_threat_score(departments)
        self.assertTrue(30 <= score <= 50)


if __name__ == '__main__':
    unittest.main()