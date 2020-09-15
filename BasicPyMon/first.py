import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]
mydict = {"name": "Peter", "address":"Lowstreet 37"}

x = mycol.insert_one(mydict)
print(x.inserted_id)

collist = mydb.list_collection_names()
dblist = myclient.list_database_names()
print(collist)
print(dblist)
