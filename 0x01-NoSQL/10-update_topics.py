#!/usr/bin/env python3
""" this is the MongoDB Operations with Python using pymongo """


def update_topics(mongo_collection, name, topics):
    """ this changes all topics of a school document based on the name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
