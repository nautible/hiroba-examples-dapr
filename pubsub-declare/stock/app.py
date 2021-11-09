import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys

app = flask.Flask(__name__)
CORS(app)

@app.route('/order', methods=['POST'])
def subscriber():
    print(request.json, flush=True)
    return json.dumps({'success':True, 'message': 'accept order'}), 200, {'ContentType':'application/json'}
app.run()