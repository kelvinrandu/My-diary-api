from flask_restful import Resource, reqparse,inputs
from flask import Flask,jsonify,request, make_response
# from model import User
from .database import DatabaseConnect
from .models import User
from psycopg2 import sql


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
        if User.find_by_email(data['email']) == 'record found' :
          return {'message': 'email {} already exists'. format(user_email)}

        new_user = User(
            username=user_name ,
            email=user_email,
            password = User.generate_hash(user_password)
     
        )
 
        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(user_name),

            }
        except:
            return {'message': 'Something went wrong'}, 500
 

class UserLogin(Resource):

    def __init__(self):
        self.cursor = db.cursor 

    def post(self):

         # validate user input
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'Please input your user name', required = True,trim=True)
        parser.add_argument('password', help = 'Please input password', required = True,trim=True)
        parser.add_argument('confirm_password', help = 'Please input  confirm password', required = True,trim=True)
        parser.add_argument('email', help = 'Please input a valid email' ,trim=True, type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), required = True)

        data = request.json
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        current_user = User.find_by_email(email)
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(email)}
        
        # if data['password'] == current_user.password:
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity = current_user.username)
            refresh_token = create_refresh_token(identity = current_user.username)
            return {'message': 'Logged in as {}'.format(current_user.username),
                    'access_token': access_token,
                    'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}
        
        return data['username']


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
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

