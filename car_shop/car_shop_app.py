from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/index.html')
def index():
    return open('index.html').read()

@app.route('/search.html')
def search():
    return open('search.html').read()

@app.route('/search_car')
def search_car():
	# search in db by given params
	return 'Nothing can be found'