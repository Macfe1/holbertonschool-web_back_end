#!/usr/bin/env python3
"""
This module provides a function to update the topics
of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name},
                                {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
