#!/usr/bin/env python3
"""list all module"""


def list_all(mongo_collection):
    """List all documents"""
    documents = list(mongo_collection.find({}))
    return documents
