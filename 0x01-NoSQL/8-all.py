#!/usr/bin/env python3
""" this is the MongoDB Operations with Python using pymongo """


def list_all(mongo_collection):
    """ this is the list all documents in Python """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
