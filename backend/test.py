from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return 'A BAD MAN FELL FROM THE SKY'

@app.route('/menus.json')
def get_menus():
	try:
		file = open("./menus.json")
		jString = file.read()
		return jString
	except:
		return '{"schiletter":["ERROR: json not found!"],"core":["ERROR: json not found!"]}'

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=80)
