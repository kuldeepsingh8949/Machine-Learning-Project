import certifi
from pymongo import MongoClient 
connection_string= "mongodb+srv://kuldeepraika64:WytraroLR6dtkhmL@farmer.pqlvj.mongodb.net/?retryWrites=true&w=majority&appName=farmer"
client = MongoClient(connection_string,tlsCAFile=certifi.where())
database = client['Farmer2']
collection = database['FarmerData1']

documents = collection.find()  # select * from table;
for document in documents: 
    print(document) 
print("thank you!") 

# execute this file to fectch your data from database 