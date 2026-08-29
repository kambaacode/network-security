import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class DBConnection:
    def __init__(self):
        load_dotenv()
        uri = os.getenv("MONGO_DB_URL")
        if not uri:
            raise ValueError("MONGO_DB_URL is missing in .env")
        self.client = MongoClient(uri, server_api=ServerApi("1"))

    def get_client(self):
        return self.client
