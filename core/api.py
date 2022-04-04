from core import Blueprint, request, jsonify, db
import uuid

api = Blueprint("api", __name__)


@api.route('' , methods=['GET'])
def home():
    data = []
    for t_db in db.test_collection.find():
        data.append(t_db)
    return jsonify({"status": "success", "data": data}), 200


@api.route('delete' , methods=['GET'])
def delete():
    item = request.args.get('item', type=str)
    if item is None:
        for t_db in db.test_collection.find():
            content = {'_id' : t_db['_id']}
            db.test_collection.delete_one(content)
    else:
        content = {'_id' : item}
        db.test_collection.delete_one(content)
    return jsonify({"status": "success", "data": "Item Deleted"}), 200


@api.route('update' , methods=['POST'])
def update_item():
    item = request.args.get('item', type=str)
    if item is None:
        return jsonify({"status": "error", "message": "No Data Found"}), 404
    else:
        data_set = db.test_collection.find_one(item)
        name = request.json['name']
        age = request.json['age']
        if name:
            data_set['name'] = name
        if age:
            data_set['age'] = age
        content = {
            '_id': uuid.uuid4().hex,
            'name': name,
            'age': age
        }
        try:
            db.test_collection.insert_one(content)
            content["_id"] = str(content["_id"])
            return jsonify({"status": "success", "data": content}), 201
        except:
            return jsonify({"status": "error", "message": "Could not Summit Request"}), 400


@api.route('add' , methods=['POST'])
def add_item():
    name = request.json['name']
    age = request.json['age']
    content = {
        '_id': uuid.uuid4().hex,
        'name': name,
        'age': age
    }
    try:
        db.test_collection.insert_one(content)
        content["_id"] = str(content["_id"])
        return jsonify({"status": "success", "data": content}), 201
    except:
        return jsonify({"status": "error", "message": "Could not Summit Request"}), 400

