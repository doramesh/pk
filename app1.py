from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection URL
db = client["mydatabase"]  # Replace with your database name
collection = db["mycollection"]  # Replace with your collection name

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
        }
        collection.insert_one(data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
