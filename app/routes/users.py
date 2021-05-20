from flask import Blueprint, jsonify, request
from app.database.user import User

module = Blueprint('users', __name__, url_prefix='/api/users')

@module.route('',methods=['GET'])
def index():
    return {'users': list(map(lambda x: x.json(), User.query.all()))}

@module.route('',methods=['POST'])
def create():
    request_data = request.get_json()
    if User.find_by_username(request_data['username']):
        return {"message": "A user with that username already exists"}, 400
    
    user = User(**request_data)
    user.save_to_db()

    return {"message": "User created successfully."}, 201