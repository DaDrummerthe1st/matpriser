"""Accessing the MongoDB_Cloud"""

import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect_to_a_mongo():
    uri = f"mongodb+srv://{st.secrets.db_username}:{st.secrets.db_password}@cluster0.ec2ax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    
    database = client["Foodprice"]
    collection = database["Products"]

    return collection