import datetime

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import make_response, jsonify
from .database import DatabaseConnect
from psycopg2 import sql


db = DatabaseConnect()


class User():

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password 
        cur = conn.cursor()
        
 

    @classmethod
    def save_to_db(cls,self):
        cur = conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO users(name, email, password)
                VALUES('me','memem','1234')""",
                (self.username, self.email,self.password))
            conn.commit()
        

        except:
            print "I can't SELECT from users"


    # check if email address exists in database 
    @staticmethod
    def find_by_email(email):

        cur.execute("""SELECT * FROM users WHERE email='{}' """.format(user_email))
        conn.commit()
        rows = cur.fetchone()
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
        self.cursor = conn.cursor()

# save to database
    @classmethod
    def create_entry(cls,title, body):
        
        self.cursor.execute(
            """
            INSERT INTO entries (name, email,password)
            VALUES (%s , %s, %s)
            """,
            (da, data['email'], data['password'])
        )
        return 'entry saved'

    @staticmethod
    def get_all(user_id):
        
        self.cursor.execute(
            """
            INSERT INTO entries (name, email,password)
            VALUES (%s , %s, %s)
            """,
            (da, data['email'], data['password'])
        )
        return 'entry saved'


    @staticmethod
    def get_each(user_id,entry_id):
        
        self.cursor.execute(
            """
            INSERT INTO entries (name, email,password)
            VALUES (%s , %s, %s)
            """,
            (da, data['email'], data['password'])
        )
        return 'entry saved'

    @staticmethod
    def post_entry(user_id,entry_id):
        
        self.cursor.execute(
            """
            INSERT INTO entries (name, email,password)
            VALUES (%s , %s, %s)
            """,
            (da, data['email'], data['password'])
        )
        return 'entry saved'


    @staticmethod
    def edit_entry(user_id,entry_id):
        
        self.cursor.execute(
            """
            INSERT INTO entries (name, email,password)
            VALUES (%s , %s, %s)
            """,
            (da, data['email'], data['password'])
        )
        return 'entry saved'

    @staticmethod
    def delete_entry(user_id,entry_id):
        
        self.cursor.execute(
            """
            INSERT INTO entries (name, email,password)
            VALUES (%s , %s, %s)
            """,
            (da, data['email'], data['password'])
        )
        return 'entry saved'

