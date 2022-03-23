from pymango import MongoClient
cclient = pymango.MongoClient("mongodb+srv://kimyeaseul:nury6710~@cluster0.jcdbs.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.kimyeaseul

doc = {
    'name' : 'bob',
    'age' : 24
}

db.users.inster_one(doc)