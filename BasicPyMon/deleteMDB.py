import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def singledelete():
    myquery = {"address":"Mountain 21"}
    mycol.delete_one(myquery)

def manydelete():
    myquery = {"address":{"regex":"^S"}}
    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")

def alldelete():
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")

alldelete()
mycol.drop()
