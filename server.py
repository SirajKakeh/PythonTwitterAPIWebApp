from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def route():
    return 'Hello, World!'

@app.route('/getBananas', methods=['GET'])
def returnBananas():
    return 'Bananas'

app.run(use_reloader=True)