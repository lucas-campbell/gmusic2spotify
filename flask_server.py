from flask import Flask
app = Flask(__name__)

#NOTE: need to `export FLASK_APP=flask_server.py`

@app.route('/')
def hello_world():
	return 'Hello dere'

@app.route('/callback')
def callback():
	return 'yes hello I am calling you back'
