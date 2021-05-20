from flask import Blueprint, jsonify, request
from app.database.item import Item
from flask_jwt import jwt_required

module = Blueprint('items', __name__, url_prefix='/api/items')

@module.route('', methods=['GET'])
@jwt_required()
def index():
    return {'items': list(map(lambda x: x.json(), Item.query.all()))}

@module.route('/<item_name>',methods=['GET'])
def show(item_name):
    item = Item.find_by_name(item_name)
    if item:
        return item.json()
    return jsonify({'message': 'Item not found'}), 404

@module.route('',methods=['POST'])
@jwt_required()
def create():
    request_data = request.get_json()
    try:
        if Item.find_by_name(request_data['name']):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
    except:
        return {"message": "the field of name is required"}
    
    try:
        new_item = Item(**request_data)
        new_item.save_to_db()
        return new_item.json(), 201
    except:
        return {"message": "An error occurred inserting the item."}, 500

@module.route('/<item_id>',methods=['DELETE'])
@jwt_required()
def delete(item_id):
    item = Item.find_by_id(item_id)
    if item:
        item.delete_from_db()
        return jsonify({'message': 'Item has been deleted'})
    return jsonify({'message': 'Item not found.'}), 404

@module.route('<item_name>',methods=['PUT'])
@jwt_required()
def update(item_name):
    request_data = request.get_json()
    item = Item.find_by_name(item_name)
    if item:
        item.price = request_data['price']
    else:
        item = Item(request_data)
    item.save_to_db()

    return item.json()


