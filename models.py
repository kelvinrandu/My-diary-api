import datetime

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import make_response, jsonify
from .database import DatabaseConnect
from psycopg2 import sql
from psycopg2 import connect


db = DatabaseConnect()


class User():

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password 
        self.cursor = db.cursor
        
 


    def save_to_db(self):
        try:
            self.cursor.execute(
                """
                INSERT INTO users(name, email, password)
                VALUES(%s,%s,%s)""",
                (self.username, self.email,self.password))
                       
            return 'register succesful'
        

        except:
            print "ran into trouble registering you"


    # check if email address exists in database 
    @staticmethod
    def find_by_email(email):
   

        db.cursor.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        # db.cursor.commit()
        rows = db.cursor.fetchone()
        
        return rows


# generate hash for user
    @staticmethod
    def generate_hash(password):
        hashed_password = generate_password_hash(password, method='sha256')
        return  hashed_password

# compare user password and hashed password from db
    @staticmethod
    def verify_hash(password, hash):
        return 2



class Entry():

    def __init__(self):
        self.title = title
        self.body = body
        self.user_id= user_id
        self.cursor = db.cursor
        

# save to database
    @classmethod
    def create_entry(cls,title, body):
        #attempt to enter entry into database
        try:
            self.cursor.execute(
                """
                INSERT INTO entrie(title, body, user_id)
                VALUES(%s,%s,%s)""",
                (self.title, self.body,self.user_id))
                       
            return 'entry added successfuly'
        

        except:
            print "ran into trouble adding entry "

    @staticmethod
    def get_all(user_id):
        
        db.cursor.execute("""SELECT * FROM entries WHERE user_id='{}' """.format(user_id))
        # db.cursor.commit()
        entries = db.cursor.fetchone()
        
        return entries


    @staticmethod
    def get_each(user_id,entry_id):
                
        db.cursor.execute("""SELECT * FROM entries WHERE id='{}' """.format(entry_id))
        # db.cursor.commit()
        entry = db.cursor.fetchone()
        
        return entry


    # @staticmethod
    # def edit_entry(user_id,entry_id):
        
    #     self.cursor.execute(
    #         """
    #         INSERT INTO entries (name, email,password)
    #         VALUES (%s , %s, %s)
    #         """,
    #         (da, data['email'], data['password'])
    #     )
    #     return 'entry saved'

    # @staticmethod
    # def delete_entry(user_id,entry_id):
        
    #     self.cursor.execute(
    #         """
    #         INSERT INTO entries (name, email,password)
    #         VALUES (%s , %s, %s)
    #         """,
    #         (da, data['email'], data['password'])
    #     )
    #     return 'entry saved'

class RevokedTokenModel():
    
    def add(self):

    
    @classmethod
    def is_jti_blacklisted(cls, jti):



