import pymongo

client = pymongo.MongoClient("mongodb+srv://yummybees123:3IE9BJXqdjWjlmKE@cluster0.i1jjohq.mongodb.net/?retryWrites=true&w=majority")

db = client.trades_database
collection_trades = db.trades
