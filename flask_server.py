from flask import Flask
app = Flask(__name__)

# NOTE: need to `export FLASK_APP=flask_server.py`
# and be sure that flask is installed on the system
#   (sudo apt install python3-flask)
# then, inside VENV run `flask run`

@app.route('/')
def hello_world():
	return 'Hello dere'

@app.route('/callback')
def callback():
	return 'yes hello I am calling you back'
