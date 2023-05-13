from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import pprint
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")


connection_string = f"mongodb+srv://yuvbindal:{password}@cluster0.xgajwdp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

#mongodb compass -> visual gui of database

dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()
print(collections)

#create a document in bson format
def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Yuv",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

insert_test_doc() 

