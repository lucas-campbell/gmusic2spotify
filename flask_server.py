from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello dere'

@app.route('/callback')
def callback():
	return 'yes hello I am calling you back'
