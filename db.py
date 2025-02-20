from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME , COLLECTION_NAME2

def get_db():
    client = MongoClient(MONGO_URI)
    return client[DB_NAME][COLLECTION_NAME]  # Returns collection reference

def get_db2():
    client = MongoClient(MONGO_URI)
    return client[DB_NAME][COLLECTION_NAME2]  # Returns collection reference
