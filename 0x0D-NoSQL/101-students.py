#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
"""
def top_students(mongo_collection):
    """ Returns all the students sorted by average score. """
    avg =  mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
    return avg
