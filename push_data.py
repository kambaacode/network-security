import os
import sys
import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecuriyException
import json

from db_connection import DBConnection
from dotenv import load_dotenv
load_dotenv()

import certifi
ca = certifi.where() # certificate authoroties

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecuriyException(e, sys)
    def csv_to_json_converter(self, file_path):
        try:
            Data = pd.read_csv(file_path)
            Data.reset_index(drop= True, inplace= True)
            records = list(json.loads((Data.T.to_json())).values())
            return records
        except Exception as e:
            raise NetworkSecuriyException(e,sys) 
    def insert_data_to_db(self, records, database_name: str, collection_name: str, database_client: pymongo):
        try:
            self.mongo_client = database_client
            self.database = self.mongo_client[database_name]
            self.collection = self.database[collection_name]
            self.collection.insert_many(records)
            return "records saved succesffully"
        except Exception as e:
            raise NetworkSecuriyException(e, sys)


DATASET_FILE_PATH = os.getenv("DATASET_FILE_PATH")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

if __name__ == "__main__":
    db_con = DBConnection()
    db_client = db_con.get_client()

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(DATASET_FILE_PATH)

    return_msg = networkobj.insert_data_to_db(records, DATABASE_NAME, COLLECTION_NAME, db_client)
    print(return_msg)