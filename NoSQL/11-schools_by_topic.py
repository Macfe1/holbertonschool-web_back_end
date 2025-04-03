#!/usr/bin/env python3
"""
This module provides a function to retrieve a list of schools
that offer a specific topic from a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools that include
    a specific topic in their curriculum.

    Args:
        mongo_collection: The pymongo collection object
        containing school documents.
        topic (str): The topic to search for in the "topics" field.

    Returns:
        list: A list of dictionaries representing the schools
        that match the criteria.
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass
