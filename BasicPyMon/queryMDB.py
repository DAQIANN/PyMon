import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def firstquery():
    myquery = {"address":"Park Lane 38"}
    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

def newquery():
    #find address starting with letter "S" or higher
    newquery = {"address":{"$gt":"S"}}
    newdoc = mycol.find(newquery)

    for y in newdoc:
        print(y)

def regexpress():
    #Starts with "S"
    myquery = {"address":{"$regex":"^S"}}
    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

regexpress()
