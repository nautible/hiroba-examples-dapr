import requests
from flask import Flask

app = Flask(__name__)

@app.route('/api-a1', methods=['GET'])
def apia1():
    
    response = requests.get('http://localhost:3500/v1.0/invoke/svc-b/method/api-b1', timeout=5)
    if not response.ok:
        print("HTTP %d => %s" % (response.status_code, response.content.decode("utf-8")), flush=True)
    
    data = response.text
    return data

if __name__ == '__main__':
    app.run()
