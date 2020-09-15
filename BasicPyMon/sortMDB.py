import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def firstsort():
    mydoc = mycol.find().sort("name")

    for x in mydoc:
        print(x)

def descsort():
    #Ascending is with 1
    mydoc = mycol.find().sort("name", -1)
    for x in mydoc:
        print(x)

descsort()
