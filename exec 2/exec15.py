from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['ciencia_dados']
collection = db['unidade_2']

import datetime

post = musica = {
              "nome": "Iron Maiden",
              "banda": "Iron Maiden",
              "categorias": ["Heavy metal", "rock"],
              "lancamento": datetime.datetime.now()
             }
post_id = collection.insert_one(post).inserted_id
post_id


#lista = [
#  { "_id": 1, "nome": "Marvin Minsky", "país": "USA"},
#  { "_id": 2, "nome": "Dennis Ritchie", "país": "USA"},
#  { "_id": 3, "nome": "Edsger Dijkstra", "país": "Netherlands"},
#  { "_id": 4, "nome": "Grace Hopper", "país": "USA"},
#  { "_id": 5, "nome": "John McCarthy", "país": "USA"}
#]
#l = collection.insert_many(lista)

#query = { "nome": "Marvin Minsky" }
#novos_valores = { "$set": { "país": "China"} }
#collection.update_one(query, novos_valores)