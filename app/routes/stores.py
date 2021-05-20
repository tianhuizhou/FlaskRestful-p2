from flask import Blueprint, jsonify, request
from app.database.store import Store
from flask_jwt import jwt_required

module = Blueprint('stores', __name__, url_prefix='/api/stores')

@module.route('', methods=['GET'])
def index():
    return {'stores': list(map(lambda x: x.json(), Store.query.all()))}
    

@module.route('/<store_id>',methods=['GET'])
def show(store_id):
    store = Store.find_by_id(store_id)
    if store:
        return store.json()
    return jsonify({'message':"A store with id '{}' already exists.".format(store_id)}),400

@module.route('',methods=['POST'])
@jwt_required()
def create():
    request_data = request.get_json()
    if Store.find_by_name(request_data['name']):
        return jsonify({'message': "A store with name '{}' already exists.".format(name)}), 400
    new_store = Store(request_data['name'])
    try:
        new_store.save_to_db()
    except:
        return jsonify({"message": "An error occurred creating the store."}), 500
    return new_store.json(), 201

@module.route('',methods=['DELETE'])
@jwt_required()
def delete():
    request_data = request.get_json()
    if Store.find_by_name(request_data['name']):
        store.delete_from_db()
        return {'message': 'Store deleted'}
    else:
        return jsonify({'message': "Store {} does not exist".format(request_data['name'])})

