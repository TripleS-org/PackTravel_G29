"""File containing helper method to load configuration"""

import os
import yaml
from pymongo import MongoClient

def get_client():
    """This method gets a handle to the database server"""
    with open(os.path.dirname(os.path.realpath(__file__)) + "/config.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    endpoint = "mongodb+srv://" + config["database"]["username"] + ":" + config["database"]["password"] + "@" + config["database"]["endpoint"]
    client = MongoClient(endpoint)
    return client
