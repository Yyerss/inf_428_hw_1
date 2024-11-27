import numpy as np


def generate_random_data(mean: int, variance: int, num_samples: int) -> np.ndarray:
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(departments, max_risk_weight=0.8):
    total_weighted_threat = 0
    total_importance = 0
    max_risk = 0

    for department in departments:
        scores = department["scores"]
        importance = department["importance"]

        avg_threat = np.mean(scores)

        total_weighted_threat += avg_threat * importance
        total_importance += importance

        max_risk = max(max_risk, avg_threat)

    weighted_average = total_weighted_threat / total_importance

    final_score = (weighted_average * (1 - max_risk_weight)) + (max_risk * max_risk_weight)
    return round(final_score, 2)

def fetch_departments_from_elasticsearch(es, index_name):
    query = {
        "size": 1000,
        "query": {"match_all": {}}
    }

    response = es.search(index=index_name, body=query)
    hits = response["hits"]["hits"]

    departments = {}
    for hit in hits:
        source = hit["_source"]
        dept = source["department"]
        score = source["score"]
        importance = source["importance"]

        if dept not in departments:
            departments[dept] = {"scores": [], "importance": importance}
        departments[dept]["scores"].append(score)

    result = [
        {"scores": data["scores"], "importance": data["importance"]}
        for data in departments.values()
    ]
    return result

