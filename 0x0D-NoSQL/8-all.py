#!/usr/bin/env python3
"""
list all documents
"""


def list_all(mongo_collection):
	"""
	return all documents in mongo collection
	"""
	x = mongo_collection.find()
	if x:
		return x
	else:
		return []
