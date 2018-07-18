from flask import Flask,jsonify

app = Flask(__name__)

#Dictionary to temporily store/hold diary entries 
Entries = [
		{
		 	'id': 1,
			'title':' Article one',
			'body':'This represents the body of the first article',
			'create_date':'04-25-2018'
		},
		{
			'id': 2,
			'title':' Article two',
			'body':'This represents the body of the second article',
			'create_date':'04-25-2018'
		},
		{
		 	'id': 3,
			'title':' Article three',
			'body':'This represents the body of the third article',
			'create_date':'04-25-2018'
		}

	]

#test route
@app.route('/')
def hello():
    return 'Hello, World!'

#route getting all entries
@app.route('/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Entries': Entries})

if __name__ == '__main__':
    app.run(debug=True)