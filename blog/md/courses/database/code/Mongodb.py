import pymongo

# Connect to MongoDB

uri="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.1"

client = pymongo.MongoClient(uri)

# Access the database and collection

db = client["shop"]

collection = db["inventory"]

# Create a document to insert

new_document = {"name": "Kevin Li", "age": 28}

# Insert the document

#result = collection.insert_one(new_document)
#print(f"Inserted document with ID: {result.inserted_id}")

collection.update_many({},{"$inc": { "age": 1 }})

searchedRecords = collection.find({})
#print(f"Find all documents in the collection： {searchedRecords}")
print(type(searchedRecords))

for document in searchedRecords:
    print(document) # iterate the cursor