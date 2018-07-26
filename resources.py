from flask_restful import Resource, reqparse
from flask import Flask,jsonify,request

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


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


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        # return {'message': 'User registration'}
        return data


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        # return {'message': 'User login'}
        return data


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'User Delete all users'}


class SecretResource(Resource):
    def get(self):
        return {'answer': 34 }

# fetch all diary entries
class AllEntries(Resource):
    def get(self):
        return jsonify({'Entries': Entries})

# fetch each diary entry
class EachEntry(Resource):
    def get(self):
        entry = [entry for entry in Entries if entry['id'] == id]
        return jsonify({'entry': entry})

# post an  entry
class PostEntry(Resource):
    def post(self):
        data = request.get_json(["data"])
        entry = data
        return jsonify({ 'message': 'entry created successfully'}), 201
   

# modify an  entry
class EditEntry(Resource):
    def put(self):
        entry = [entry for entry in Entries if entry['id'] == id]
        me = request.get_json(['tittle'])
        entry[0]['Body'] = me['Body']    
        return jsonify({ "message" : "entry modified successfully" }), 200

# delete an  entry
class DeleteEntry(Resource):
    def delete(self):
        entry = [entry for entry in Entries if entry['id'] == id]
        Entries.remove(entry[0])
        return jsonify({ "message" : " entry deleted successfully" })

