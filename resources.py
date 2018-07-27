from flask_restful import Resource, reqparse
from flask import Flask,jsonify,request, make_response
# from model import User
from .database import DatabaseConnect
from psycopg2 import sql

db = DatabaseConnect()

parser = reqparse.RequestParser()
# parser.add_argument('username', help = 'This field cannot be blank', required = True)
# parser.add_argument('password', help = 'This field cannot be blank', required = True)
# parser.add_argument('email', help = 'This field cannot be blank', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        
        db.conn.cursor().execute(
        """INSERT INTO users (name, email, password) 
            VALUES ('kelvin', 'ke5n@m.com', 'hdsghks')"""
        )

        response = {'message': 'user created'}
        
        return response


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        # return {'message': 'User login'}
        id = self.
        self.cursor.execute(
            sql.SQL("select * from users where id={}").format(sql.Placeholder()), 
            ([id])
        )
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
    def __init__(self):
        self.cursor = db.cursor        

    def post(self):
        data = request.json

        self.cursor.execute(
            sql.SQL("insert into entries(title, body) values({}) returning id").format(
                sql.SQL(', ').join(sql.Placeholder() * 2)
            ), ([data['title'], data['body']])
        )

        id = self.cursor.fetchone()['id']

        self.cursor.execute(
            sql.SQL("select * from entries where id={}").format(sql.Placeholder()), 
            ([id])
        )
        
        entry = self.cursor.fetchone()

        return make_response(jsonify({'entry': entry}))
   

# modify an  entry
class EditEntry(Resource):
    def put(self):
        data = request.json
        id = data['id']

        result = self.cursor.execute(
            sql.SQL("select * from entries where id={}").format(sql.Placeholder()), 
            ([id])
        )

        if result:

            self.cursor.execute(
                sql.SQL("update table entries set {} values({}) returning id").format(
                sql.SQL(', ').join(sql.Placeholder() * 2)
                 ), ([data['title'], data['body']])
            )
            return jsonify({ "message" : " entry updated successfully" })
        



# delete an  entry
class DeleteEntry(Resource):
    def delete(self):
        entry = [entry for entry in Entries if entry['id'] == id]
        Entries.remove(entry[0])
        return jsonify({ "message" : " entry deleted successfully" })

