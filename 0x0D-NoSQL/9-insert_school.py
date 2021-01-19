#!/usr/bin/env python3
"""
insert new document in collection.
"""


def insert_school(mongo_collection, **kwargs):
	"""
	insert new document in collection based on kwargs.
	"""
	_id = None
	if mongo_collection and kwargs:
		_id = mongo_collection.insert_one(kwargs).inserted_id
	return _id
