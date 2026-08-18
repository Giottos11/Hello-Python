import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URI"))

db_client = client["users_db"]

