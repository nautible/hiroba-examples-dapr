import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys

app = flask.Flask(__name__)
CORS(app)

@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    print("checkd subscribe")
    subscriptions = [{'pubsubname': 'order-pubsub',
                      'topic': 'order',
                      'route': 'order'}]
    return jsonify(subscriptions)

@app.route('/order', methods=['POST'])
def ds_subscriber():
    print(request.json, flush=True)
    return json.dumps({'success':True, 'message': 'accept order'}), 200, {'ContentType':'application/json'}
app.run()