from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://mongodb:27017")
db = client.test_db

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Analytics POC"}

@app.get("/data")
def get_data():
    data = db.test_collection.find()
    return [{"key": item["key"], "value": item["value"]} for item in data]
