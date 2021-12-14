from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'ooc store',
        'items': [{
            'name': 'oocs panda',
            'price': 999
        }]
    }
]

users = [
    {
        'name': 'user1001',
        'user_info':
            {
                'uuid': 1001,
                'email_id': 'user1001@oocs.com',
                'company': 'oocs'
            }
    }
]


@app.route('/')
def home():
    return render_template('index.html')


# create a store
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# get a store by name
@app.route("/store/<string:name>", methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'Store not found'}), 404


# get all stores
@app.route("/store")
def get_all_stores():
    return jsonify({'stores': stores})


# create item in a store
@app.route("/store/<string:name>/item", methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
        else:
            return jsonify({'message': 'Store not found'})


# get item from the store
@app.route("/store/<string:name>/item", methods=['GET'])
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': 'Store not found'})


@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({'users': users})


@app.route('/users/<string:name>', methods=['GET'])
def get_user_by_name(name):
    for user in users:
        if user['name'] == name:
            return jsonify({'users': user}), 200
    return jsonify({'message': 'user not found'}), 404


@app.route('/users', methods=['POST'])
def create_new_user():
    request_body = request.get_json()
    new_user = {
        'name': request_body['name'],
        'user_info':
            {
                'uuid': request_body['user_info']['uuid'],
                'email_id': request_body['user_info']['email_id'],
                'company': request_body['user_info']['company']
            }
    }

    if new_user not in users:
        users.append(new_user)
        return jsonify({'message': 'Successfully added new user!'},
                       {'users': new_user}), 201
    else:
        return jsonify({'message': 'User already created'}), 422

@app.route('/users/<string:name>', methods=['PUT'])
def update_user_details(name):
    for user in users:
        if user['name'] == name:
            request_body = request.get_json()
            update_user = {
                'name': request_body['name']
            }
            user.update(update_user)
            return jsonify({'message': 'Successfully updated user!'},
                           {'users': user['name']}), 200
        else:
            return jsonify({'message': 'user not found'}), 404

app.run(port=5000, debug=False)