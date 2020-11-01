from flask import Flask, request


app = Flask(__name__)


import cars_db_sqlite as db


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/index.html')
def index():
    return open('index.html').read()

@app.route('/search.html')
def search():
    return open('search.html').read()

@app.route('/search_car_by_price')
def search_car():
	price1 = int(request.args['price1'])
	price2 = int(request.args['price2'])
	# search in db by given params
	return convert_to_table(db.search_by_price(price1, price2))

@app.route('/sort_by_year')
def sort_by_year():

	return convert_to_table(db.sort_by_year())


def convert_to_table(cars):
	def td(x):
		return f"<td>{x}</td>"

	rows = ''
	for car_info in cars:
		row = ''
		for elem in car_info:
			row += td(elem)
		rows += f'<tr>{row}</tr>'
	return f'<table border="1px">{rows}</table>'