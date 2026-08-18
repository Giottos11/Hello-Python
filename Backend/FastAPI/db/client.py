from pymongo import MongoClient

client = MongoClient("mongodb+srv://giottos330_db_user:QZtcfvdDvgtIdK4o@cluster0.iab2yrf.mongodb.net/?appName=Cluster0")

db_client = client["users_db"]