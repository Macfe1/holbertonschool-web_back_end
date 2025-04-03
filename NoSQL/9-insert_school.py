#!/usr/bin/env python3
"""
This module provides a function to insert
a new document into a given collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified collection.

    Args:
        mongo_collection: The collection where the document
        will be inserted.
        **kwargs: Arbitrary keyword arguments representing
        the document fields.

    Returns:
        ObjectId: The unique identifier(_id) of the inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    pass
