from flask import Flask
app = Flask(__name__)

@app.route('/api-b1', methods=['GET'])
def apib1():
     return 'svc-b api-b1 called!'

if __name__ == '__main__':
    app.run()
