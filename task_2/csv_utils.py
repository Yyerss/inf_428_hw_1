import csv
import numpy as np
from .utils import generate_random_data


def generate_and_save_csv(file_path):
    departments = ["Engineering", "Marketing", "Finance", "HR", "Science"]
    data = []

    for dept in departments:
        scores = generate_random_data(mean=50, variance=20, num_samples=np.random.randint(10, 200))
        importance = np.random.randint(1, 6)
        for score in scores:
            data.append([dept, score, importance])

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["department", "score", "importance"])
        writer.writerows(data)

