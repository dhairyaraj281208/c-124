from datetime import timedelta
from flask import Flask, json, jsonify,request
app = Flask(__name__)

contacts = [
    {
        'id': 1, 
        'contact':'9351577723',
        'name': 'Dhairya',
        'done': False
    },
    {
        'id': 2, 
        'contact':'7737911591',
        'name': 'Shaurya',
        'done': False
    }
]
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)

    contact = {
        'id': contacts[-1]['id']+1,
        'Name': request.json['name'],
        'Contact': request.json.get('contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "task added succesfully"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data": contacts
    })

if __name__ == '__main__':
    app.run(debug=True)