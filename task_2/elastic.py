from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv

def create_index(es, index_name):
    mappings = {
        "mappings": {
            "properties": {
                "department": {"type": "keyword"},
                "score": {"type": "integer"},
                "importance": {"type": "integer"}
            }
        }
    }
    es.indices.create(index=index_name, body=mappings, ignore=400)

def populate_index_from_csv(es, index_name, file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        actions = [
            {
                "_index": index_name,
                "_source": {
                    "department": row["department"],
                    "score": int(row["score"]),
                    "importance": int(row["importance"]),
                },
            }
            for row in reader
        ]

    bulk(es, actions)
