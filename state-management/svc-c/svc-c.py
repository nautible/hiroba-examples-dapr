import requests
from flask import Flask,jsonify,request

app = Flask(__name__)

login_user_id = 'A00001'

@app.route('/save', methods=['POST'])
def save():
    
    r_data = request.json
    product_id = r_data.get('product_id')
    quantity = r_data.get('quantity') 
    # 受信したデータをDaprに連携するためjson形式にする
    data = [{'key': login_user_id, 'value': [{'product_id': product_id, 'quantity': quantity }]}]
    # Daprサイドカーのデータ保存用URLを呼び出す
    response = requests.post('http://localhost:3500/v1.0/state/{statestore}'.format(statestore = 'cart'), json = data, timeout=5)
    if not response.ok:
        print('HTTP %d => %s' % (response.status_code, response.content.decode('utf-8')), flush=True)
    
    return 'OK'

@app.route('/get', methods=['GET'])
def get():
    # Daprサイドカーのデータ取得用URLを呼び出す
    response = requests.get('http://localhost:3500/v1.0/state/{statestore}/{key}'.format(statestore = 'cart', key = login_user_id),  timeout=5)
    if not response.ok:
        print('HTTP %d => %s' % (response.status_code, response.content.decode('utf-8')), flush=True)
    data = response.text
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
