import os 
import json
import sys

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(f"MONGO_DB_URL: {MONGO_DB_URL}")

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity .logging.logger import logging

class Network_data_extract():
    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records 
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongoDB(self,records,database,collection):
        try: 
            self.database = database 
            self.collection = collection 
            self.records = records 
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database = self.mongo_client[self.database] 
            self.collection = self.database[self.collection] 
            self.collection.insert_many(self.records) 
            return len(self.records) 
        except Exception as e: raise NetworkSecurityException(e)


if __name__=="__main__":
    try:
        File_Path="network_data\phisingData.csv"
        DataBase="Rudra_pahuja"
        collection="NetworkData"
        network_obj=Network_data_extract()
        records=network_obj.csv_to_json_converter(File_Path)
        print(records[0])
        count=network_obj.insert_data_to_mongoDB(records,DataBase,collection)
        print(f"Total records inserted to MongoDB are : {count}")
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)