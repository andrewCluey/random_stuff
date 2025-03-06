
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import argparse
 
parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("connection", help="The full mongodb connection string to test.")
args = vars(parser.parse_args())

connection = args["connection"]

# Create a new client and connect to the server
client = MongoClient(connection, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    result = client.admin.command('ping')
    print(result)
    
except Exception as e:
    print(e)
