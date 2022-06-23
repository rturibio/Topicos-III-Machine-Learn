from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['ciencia_dados']
collection = db['unidade_2']

import datetime

query = {"nome": "Iron Maiden"}
collection.delete_one(query)