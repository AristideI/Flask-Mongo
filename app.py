from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://aisingizwe:xAizVlslg0mZNgbX@cluster0.gtjojsg.mongodb.net/flask?retryWrites=true&w=majority&appName=Cluster0')

#mongo db database
db = client.flask_database
#todos collenction
todos = db.todos

if __name__ == "__main__":
          app.run(debug=True)
