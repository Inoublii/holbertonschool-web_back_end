#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def getlogs():
    """ Provides some stats about Nginx logs stored in MongoDB. """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(nginx.count_documents({})," logs")

    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, nginx.count_documents({'method': method})
            )
        )

    print(
        nginx.count_documents(
            {'method': 'GET', 'path': '/status'})," status check"
        )
if __name__ == "__main__":
    getlogs()
