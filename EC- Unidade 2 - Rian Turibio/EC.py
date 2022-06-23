from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')

db = client['database']
collection = db['collection']

import datetime

#with open('2015_USPTOf.json') as f:
#   file_data = json.load(f)

#collection.insert_many(file_data)

#resp = collection.create_index(
#[("Title", 1),("Abstract", 1)])
#print ("index response:", resp)

#post = {
 #             "Subclass_labels": [
 #             "001", 
 #             "002"
 #              ], 
 #             "Abstract": "teste1", 
 #             "Title": "teste2", 
 #             "No": "teste3"
 #            }
#post_id = collection.insert_one(post).inserted_id
#post_id

card = db.collection.find_one({"Title": "aircrew ensembles"})
print(card)