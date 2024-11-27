from task_2.elastic import create_index, populate_index_from_csv
from task_2.utils import calculate_aggregated_threat_score, fetch_departments_from_elasticsearch
from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch("http://localhost:9200")
    file_path = "threat_data.csv"

    index_name = "threat_scores"
    create_index(es, index_name)
    populate_index_from_csv(es, index_name, file_path)

    departments = fetch_departments_from_elasticsearch(es, index_name)

    print("Aggregated Threat Score:", calculate_aggregated_threat_score(departments))


if __name__ == "__main__":
    main()
