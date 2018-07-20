from flask import Flask,jsonify,request

app = Flask(__name__)
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




if __name__ == '__main__':
    app.run(debug=True)