#!/usr/bin/env python3
""""
This module contains a function to list all documents
from a given MongoDB collection.
"""
if __name__ == "__main__":

    def list_all(mongo_collection):
        """
        Lists all documents in a collection.

        Args:
            mongo_collection: The collection to retrieve documents from.

        Returns:
            list: A list of all documents in the collection,
            or an empty list if there are none.
        """
        return list(mongo_collection)
