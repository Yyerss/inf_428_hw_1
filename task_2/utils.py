import numpy as np
from typing import List, Dict


def generate_random_data(mean: int, variance: int, num_samples: int) -> np.ndarray:
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(departments: List[Dict[str, any]]) -> float:
    total_score = 0
    total_importance = 0

    for department in departments:
        mean_score = np.mean(department['scores'])
        weighted_score = mean_score * department['importance']
        total_score += weighted_score
        total_importance += department['importance']

    aggregated_score = total_score / total_importance if total_importance != 0 else 0
    return min(max(aggregated_score, 0), 90)