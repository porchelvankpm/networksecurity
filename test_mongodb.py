from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://porchelvankpm:Porch1994@cluster0.2ldno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# uri = "mongodb://localhost:27017"

# Create a new client with SSL verification disabled
client = MongoClient(uri, tlsAllowInvalidCertificates=True)
# client = MongoClient(uri)

# from pymongo.mongo_client import MongoClient
# import certifi

# # Correct MongoDB Atlas URI
# uri = "mongodb+srv://porchelvankpm:Porch1994@cluster0.2ldno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Ensure the MongoClient uses the correct URI
# client = MongoClient(uri, tlsCAFile=certifi.where())


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error: {e}")
