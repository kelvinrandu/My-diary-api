
from flask import Flask,jsonify,request

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

#post entry endpoint
@app.route('/api/v1/entries', methods=['POST'])
def post_entry():
    data = request.get_json(["data"])
    entry = data
    return jsonify({ 'status': 'entry created successfully'}), 201



#route getting all entries
@app.route('/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Entries': Entries})

#delete entry route
@app.route('/api/v1/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    entry = [entry for entry in Entries if entry['id'] == id]
    Entries.remove(entry[0])
    return jsonify({ "status" : "true" })


if __name__ == '__main__':
    app.run(debug=True)