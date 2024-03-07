from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Alice", "age": 25},
    {"id": 3, "name": "Bob", "age": 35},
]

@app.route("/users", methods=['GET'])
def get_users():
    return jsonify(users)

@app.route("/users", methods=['POST'])
def create_user():
    new_user =  {
            'id': len(users) + 1,
            'name': request.json['name'],
            'age': request.json['age'],
        }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    for user in users: 
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    for user in users: 
        if user["id"] == user_id:
            user["name"] = request.json['name']
            user["age"] = request.json['age']
            return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    for user in users: 
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"response": "User deleted"})
    return jsonify({'error': 'User not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
