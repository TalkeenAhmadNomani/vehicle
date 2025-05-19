import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URI_KEY


ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URI_KEY  # Use hardcoded URI here
                print(f"MongoDB URL used: {mongo_db_url}")  # Debug print

                # if not (mongo_db_url.startswith("mongodb://") or mongo_db_url.startswith("mongodb+srv://")):
                #     raise Exception("Invalid MongoDB URI: must start with 'mongodb://' or 'mongodb+srv://'")

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                logging.info("MongoDB client created successfully.")

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Connected to MongoDB database: {database_name}")

        except Exception as e:
            raise MyException(e, sys)
