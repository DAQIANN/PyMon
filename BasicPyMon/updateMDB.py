import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def upone():
    myquery = {"address":"Valley 345"}
    newvalues = {"$set":{"address":"Canyon 123"}}
    mycol.update_one(myquery, newvalues)

def upmany():
    myquery = {"address":{"$regex":"^S"}}
    newvalues = {"$set":{"name":"Minnie"}}
    x = mycol.update_many(myquery, newvalues)
    print(x.modified_count, " docs updated.")

#upone()
upmany()
for x in mycol.find():
    print(x)
