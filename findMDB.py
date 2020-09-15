import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
#x = mycol.find_one()

#print(x)

#for x in mycol.find():
    #print(x)

#Only prints out the name and address, can only be both 0 or 1
for x in mycol.find({}, {"_id":0, "name":1, "address":1}):
    print(x)
