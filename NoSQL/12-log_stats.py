#!/usr/bin/env python3
"""
This script provides basic statistics about Nginx logs
stored in a MongoDB collection.
It connects to the 'logs.nginx' collection and displays:
- The total number of log documents
- The number of documents by HTTP method (GET, POST, PUT, PATCH, DELETE)
- The number of documents with method=GET and path=/status
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

total_documentos = len(list(collection.find({})))
total_get = len(list(collection.find({"method": "GET"})))
total_post = len(list(collection.find({"method": "POST"})))
total_put = len(list(collection.find({"method": "PUT"})))
total_patch = len(list(collection.find({"method": "PATCH"})))
total_delete = len(list(collection.find({"method": "DELETE"})))
status = len(list(collection.find({"method": "GET", "path": "/status"})))

print(f"{total_documentos} logs")
print("Methods:")
print(f"\tmethod GET: {total_get}")
print(f"\tmethod POST: {total_post}")
print(f"\tmethod PUT: {total_put}")
print(f"\tmethod PATCH: {total_patch}")
print(f"\tmethod DELETE: {total_delete}")
print(f"{status} status check")

if __name__ == "__main__":
    pass
