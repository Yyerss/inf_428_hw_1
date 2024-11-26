import numpy as np
from typing import List, Dict


def generate_random_data(mean: int, variance: int, num_samples: int) -> np.ndarray:
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(departments, penalty_weight=2.0):
    total_weighted_sum = 0
    total_importance = 0
    max_threat = 0

    for department in departments:
        scores = department["scores"]
        importance = department["importance"]
        average_score = np.mean(scores)

        total_weighted_sum += average_score * importance
        total_importance += importance

        max_threat = max(max_threat, average_score)

    weighted_average = total_weighted_sum / total_importance
    final_score = (weighted_average + penalty_weight * max_threat) / (1 + penalty_weight)
    return round(final_score, 2)
