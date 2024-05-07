#!/usr/bin/env python3
"""insert document module"""


def insert_school(mongo_collection, **kwargs):
    """insert document function"""
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value
    new_obj = mongo_collection.insert_one(my_dict)
    return new_obj.inserted_id
