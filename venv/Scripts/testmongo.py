import pymongo
from pymongo import MongoClient
from pandas import DataFrame
print(pymongo.version)

client = MongoClient('mongodb+srv://admin:kHZ752GRiRy6jgOt@cluster0.k22ipw1.mongodb.net/?retryWrites=true&w=majority')
cnt = 0
#print (client)
for item in client.list_database_names():
  print(item)
#print(client['user_shopping_list'])
#dbname = client['user_shopping_list']
dbname = client['sample_airbnb']
#for item in dbname.list_collections():
#   print(item)
print(dbname.list_collection_names())
#collection_name = dbname["user_1_items"]
collection_name = dbname["listingsAndReviews"]
item_details = collection_name.find({'_id': '10006546'})

print(collection_name.database.name)
# for item in item_details:
#     # This does not give a very readable output
#     print(item )
#     cnt = cnt + 1
#     if cnt > 10 :
#       break
items_df = DataFrame(item_details)
print(items_df.to_csv("c:\\projects\\check.txt"))