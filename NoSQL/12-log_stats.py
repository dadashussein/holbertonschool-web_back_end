#!/usr/bin/env python3
"""change topics module"""
from pymongo import MongoClient


def get_nginx_stats():
    """get ngnix stats"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_logs_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_logs_count} status check")


if __name__ == "__main__":
    get_nginx_stats()
