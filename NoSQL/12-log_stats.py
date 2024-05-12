#!/usr/bin/env python3
"""change topics module"""
from pymongo import MongoClient


def get_nginx_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngnix_collection = client.logs.nginx

    total_count = ngnix_collection.count_documents({})
    get_count = ngnix_collection.count_documents({
        "method": "GET"
    })
    post_count = ngnix_collection.count_documents({
        "method": "POST"
    })
    put_count = ngnix_collection.count_documents({
        "method": "PUT"
    })
    patch_count = ngnix_collection.count_documents({
        "method": "PATCH"
    })
    delete_count = ngnix_collection.count_documents({
        "method": "DELETE"
    })
    path_status = ngnix_collection.count_documents({
        "path": "/status"
    })
    print(f"{total_count} logs")
    print("Methods:")
    print(f"\tmethod GET:{get_count}")
    print(f"\tmethod POST:{post_count}")
    print(f"\tmethod PUT:{put_count}")
    print(f"\tmethod PATCH:{patch_count}")
    print(f"\tmethod DELETE:{delete_count}")
    print(f"{path_status} status check")


if __name__ == "__main__":
    get_nginx_stats()
