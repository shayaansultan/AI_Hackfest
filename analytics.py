import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mongo
import datetime

# Get data from MongoDB
def create_dataframe(username):
    df = pd.DataFrame(columns=["Username","Date", "Product", "Price"])
    receipts = mongo.get_receipts(username)
    for receipt in receipts:
        username = receipt["username"]
        date = receipt["date"]
        products = receipt["products"]
        for product in products:
            product_name = product
            product_price = products[product]
            df.loc[len(df.index)] = [username, date, product_name, product_price]
    return df

print(create_dataframe("yuvbindal"))