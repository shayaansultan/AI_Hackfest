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
#print(dbs)
hackathon_db = client.hackathon
collections = hackathon_db.list_collection_names()
#print(collections)

#create a document in bson format
def insert_test_doc():
#    collection = test_db.test
    test_document = {
        "name": "Yuv",
        "type": "Test"
    }
#    inserted_id = collection.insert_one(test_document).inserted_id
#    print(inserted_id)

#insert_test_doc() 

def insert_receipt(username, date, product_dict):
    collection = hackathon_db.receipts
    receipt_document = {
        "username": f"{username}",
        "date": f"{date}",
        "products": product_dict
    }
    inserted_id = collection.insert_one(receipt_document).inserted_id
    #print(f"Inserted ID: {inserted_id}")

#insert_receipt("yuvbindal", "2023-11-10", {"mixed fruits": 19.99, "laundry detergent": 9.99, "milk": 3.99})
#insert_receipt("yuvbindal", "2020-11-20", {"shirt": 14.99, "jeans": 9.99})
#insert_receipt("yuvbindal", "2020-11-30", {"video games": 5.99, "books": 4.99})

def insert_user(username, password):
    collection = hackathon_db.users
    user_document = {
        "username": f"{username}",
        "password": f"{password}"
    }
    inserted_id = collection.insert_one(user_document).inserted_id
    #print(f"Inserted ID: {inserted_id}")



def check_user(username, password):
    collection = hackathon_db.users
    user = collection.find_one({"username": f"{username}"})
    if user is None:
        return False
    elif user["password"] == password:
        return True
    else:
        return False
    
def get_receipts(username) :
    collection = hackathon_db.receipts
    receipts = collection.find({"username": f"{username}"})
    return receipts 


