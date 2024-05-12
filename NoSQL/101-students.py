#!/usr/bin/env python3
"""Document module"""


def top_students(mongo_collection):
    """function document"""
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students
