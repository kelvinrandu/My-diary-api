from flask_restful import Resource, reqparse
from flask import Flask,jsonify,request, make_response
import re
# from model import User
from database import DatabaseConnect
from models import User
from models import Entry
from psycopg2 import sql
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity)


db = DatabaseConnect()


class UserRegistration(Resource):
    

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True, help='Email cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank', type=str)
  

    # handle create user logic

    def post(self):
        

        # remove all whitespaces from input
        args =  UserRegistration.parser.parse_args()
        password = args.get('password')
        confirm_password = args.get('confirm_password')
        username = args.get('username').strip()
        email = args.get('email').strip()



        # validate user input
        email_format = re.compile(
        r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
        username_format = re.compile(r"(^[A-Za-z0-9-]+$)")


        if not email:
            return make_response(jsonify({'message': 'email can not be empty'}),400)
        if not password:
            return make_response(jsonify({'message': 'password cannot be empty'}),400)
        if not username:
            return make_response(jsonify({'message': 'username cannot be empty'}),400)
        if len(password) < 6:
            return make_response(jsonify({'message' : 'Password should be atleast 6 characters'}), 400)
        if not (re.match(email_format, email)):
            return make_response(jsonify({'message' : 'Invalid email'}), 400)
        if not (re.match(username_format, username)):
            return make_response(jsonify({'message' : 'Please input only characters and numbers'}), 400)

            


        # check if email already exists
        if User.find_by_email(email) :
          return {'message': 'email {} already exists'. format(email)}
 
        # send validated user input to user model
        new_user = User(
            username=username ,
            email=email,
            password = User.generate_hash(password)
     
        )

        # attempt creating a new user in user model
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = username)
            return {
                'message': 'User {} was created'.format(username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
 
# handle user login
class UserLogin(Resource):
    
    # validate user input
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank')


    def post(self):

        # check for white spaces
        args =  UserLogin.parser.parse_args()
        password = args.get('password').strip()
        email = args.get('email').strip()
        if not email:
            return {'message': 'email can not be empty'},400
        if not password:
            return {'message': 'password cannot be empty'},400


        # upon successful validation check if user by the email exists in database and return response if not
        current_user = User.find_by_email(email)
        if current_user is None:
            return {'message': 'email {} doesn\'t exist'.format(email)},400

        
        # compare user's password and the hashed password in database
        if User.verify_hash(password, current_user['password']):
            access_token = create_access_token(identity =  current_user['name'])
            refresh_token = create_refresh_token(identity = current_user['name'])
            return {
                'message': 'Logged in as {}'.format(current_user['name']),
                'access_token': access_token,
                'refresh_token': refresh_token

                },200
        else:
            return {'message': 'Wrong credentials'},400

# handle user logout
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
    @jwt_required
    def get(self):
        return {'answer': 34 }

# fetch all diary entries
class AllEntries(Resource):
    @jwt_required
    

    def get(self):
        #user_id from session
        
        if Entry.get_all() :
            rows=  Entry.get_all()
            return jsonify({'message':rows })
        return jsonify({'message':'no entries yet'})
        

# fetch each diary entry
class EachEntry(Resource):
    def get(self,entry_id):
        rows=  Entry.get_each(entry_id)
        if rows:
            return jsonify({'message':rows })
        else:
            return jsonify({'message':'not found' }),404


# post an  entry
class PostEntry(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, help='title cannot be blank', type=str)
    parser.add_argument('body', required=True, help='body cannot be blank', type=str)
    parser.add_argument('user_id', required=True, help='user cannot be blank', type=int)      
    @jwt_required
    def post(self):

        args =  PostEntry.parser.parse_args()
        title = args.get('title').strip()
        body = args.get('body').strip()
        user = args.get('user_id')

        if not body:
            return make_response(jsonify({'message': 'body can not be empty'}),400)
        if not user:
            return make_response(jsonify({'message': 'user id cannot be empty'}),400)
        if not title:
            return make_response(jsonify({'message': 'title cannot be empty'}),400)

        new_entry = Entry(
            title=title ,
            body=body,
            user_id = user
     
        )
        # attempt creating a new user through user model
        try:
            Entry.save_entry_to_db(title,body,user)


            return {
                'message': 'Entry {} was created'.format(title)

                }

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

   

# modify an  entry
class EditEntry(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, help='title cannot be blank', type=str)
    parser.add_argument('body', required=True, help='body cannot be blank', type=str)


    @jwt_required
    def put(self,entry_id):

        args =  EditEntry.parser.parse_args()
        title = args.get('title').strip()
        body = args.get('body').strip()
        entry_id = entry_id

        # attempt creating a new user through user model
        try:
            Entry.edit_entry(title,body,entry_id)

            return {
                'message': 'Entry  was successfuly edited'

                }

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


# delete an  entry
class DeleteEntry(Resource):
    @jwt_required
    def delete(self,entry_id):
        try:
            Entry.delete_entry(entry_id)

            return {
                'message': 'Entry  was successfuly deleted'

                }

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


