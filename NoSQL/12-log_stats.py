#!/usr/bin/env python3
"""
This script provides basic statistics about Nginx
logs stored in a MongoDB collection.

It connects to the MongoDB instance running locally,
accesses the 'logs' database and
the 'nginx' collection. It then calculates and displays:

- The total number of documents (logs)
- The number of logs for each HTTP method: GET, POST, PUT, PATCH, DELETE
- The number of logs with method=GET and path=/status
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

total_documentos = collection.count_documents({})
total_get = collection.count_documents({"method": "GET"})
total_post = collection.count_documents({"method": "POST"})
total_put = collection.count_documents({"method": "PUT"})
total_patch = collection.count_documents({"method": "PATCH"})
total_delete = collection.count_documents({"method": "DELETE"})
status = collection.count_documents({"method": "GET", "path": "/status"})

print(total_documentos, "logs")
print("Methods:")
print(f"\tmethod GET: {total_get}")
print(f"\tmethod POST: {total_post}")
print(f"\tmethod PUT: {total_put}")
print(f"\tmethod PATCH: {total_patch}")
print(f"\tmethod DELETE: {total_delete}")
print(f"{status} status check")


if __name__ == "__main__":
    pass
