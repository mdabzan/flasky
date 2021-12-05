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
            return jsonify({'message': 'Store not found'})


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


app.run(port=5000, debug=False)
