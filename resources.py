from flask_restful import Resource, reqparse,inputs
from flask import Flask,jsonify,request, make_response
# from model import User
from .database import DatabaseConnect
from .models import User
from psycopg2 import sql
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


db = DatabaseConnect()



class UserRegistration(Resource):

    def __init__(self):
        self.cursor = db.cursor 
        

    def post(self):
        # validate user input
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'Please input your user name', required = True,trim=True)
        parser.add_argument('password', help = 'Please input password', required = True,trim=True)
        parser.add_argument('confirm_password', help = 'Please input  confirm password', required = True,trim=True)
        parser.add_argument('email', help = 'Please input a valid email' ,trim=True, type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), required = True)

        # store input in variable for easy manipulation    
        data = request.json
        user_name =  data['username']
        user_email = data['email']
        user_password = data['password']
        confirm_password = data['confirm_password']

        # check if email already exists
        if User.find_by_email(user_email) == 'email exists' :
          return {'message': 'email {} already exists'. format(user_email)}

        new_user = User(
            username=user_name ,
            email=user_email,
            password = User.generate_hash(user_password)
     
        )

        # attempt creating a new user through respective model
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = user_name)
            refresh_token = create_refresh_token(identity = user_name)
            return {
                'message': 'User {} was created'.format(user_name),
                'access_token': access_token,
                'refresh_token': refresh_token
                }

        except:
            return {'message': 'Something went wrong'}, 500
 

class UserLogin(Resource):

    def __init__(self):
        self.cursor = db.cursor 

    def post(self):

        # validate user input
        parser = reqparse.RequestParser()
        parser.add_argument('password', help = 'Please input password', required = True,trim=True)
        parser.add_argument('email', help = 'Please input a valid email' ,trim=True, type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), required = True)
 
        # upon succesful validation get user input and store in variable
        data = request.json
        email = data['email']
        password = data['password']

        # check if user by the email exists in database and return response if not
        current_user = User.find_by_email(email)
        if current_user is None:
            return {'message': 'User {} doesn\'t exist'.format(email)}
        
        # compare user's password and the hashed password in database
        if User.verify_hash(password, current_user['password']):
            access_token = create_access_token(identity =  current_user['name'])
            refresh_token = create_refresh_token(identity = current_user['name'])
            return {
                'message': 'Logged in as {}'.format(current_user['name']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):

        jti = get_raw_jwt()['jti']
        try:
            revoked_token = User(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500



class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
       jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}



class SecretResource(Resource):
    def get(self):
        return {'answer': 34 }

# fetch all diary entries
class AllEntries(Resource):
    
    def __init__(self,user_id,entry):
        self.cursor = db.cursor 



    def get(self):
        cur.execute("""SELECT * FROM entries WHERE user_id={} """.format(user_id))
        entry = cur.fetchone()
        return jsonify({'Entries': entry})

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
        entry = [entry for entry in Entries if entry['id'] == id]
        Entries.remove(entry[0])
        return jsonify({ "message" : " entry deleted successfully" })

