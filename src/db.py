from pymongo import MongoClient
import json

class MongoDBHandler:
    def __init__(self):
        self.client = MongoClient("mongodb://root:example_password@localhost:27017/")
        self.db = self.client.gpw_analytics
        self.collection = self.db.reports

    def insert_report(self, report_data):
        if isinstance(report_data, str):
            report_data = json.loads(report_data)
        result = self.collection.insert_one(report_data)
        print(f"Zapisano raport w MongoDB. ID: {result.inserted_id}")
        return result.inserted_id
