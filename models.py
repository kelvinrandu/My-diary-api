import datetime
from flask import make_response, jsonify
from database import DatabaseConnect
from psycopg2 import sql
from psycopg2 import connect
from passlib.hash import pbkdf2_sha256 as sha256

db = DatabaseConnect()



class User():

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password 

  
        
 


    def save_to_db(self):
        try:
            db.cursor.execute(
                """
                INSERT INTO users(name, email, password)
                VALUES(%s,%s,%s)""",
                (self.username, self.email,self.password))
            # db.CloseConnection()

            
                       
            return 'register succesful'
        

        except:
            print ("ran into trouble registering you")


    # check if email address exists in database 
    @staticmethod
    def find_by_email(email):
   

        db.cursor.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        # db.cursor.commit()
        rows = db.cursor.fetchone()

               
        return rows
        

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class Entry():

    def __init__(self,title,body,user_id):
        self.title = title
        self.body = body
        self.user_id= user_id

        

    def save_entry_to_db(title,body,user):
        try:
            db.cursor.execute(
                """
                INSERT INTO entries(title, body, created_by)
                VALUES(%s,%s,%s)""",
                (title, body,user))
            # db.CloseConnection()

            
                       
            return 'created entry succesfully'
        

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


    @staticmethod
    def get_all():
        try:
      
            db.cursor.execute("""SELECT * FROM entries  """)
            # db.cursor.commit()
            rows = db.cursor.fetchall()


            return rows
        

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500



    @staticmethod
    def get_each(entry_id):
        try:
      
            db.cursor.execute("""SELECT * FROM entries WHERE id='{}' """.format(entry_id))
            # db.cursor.commit()
            rows = db.cursor.fetchall()
        
            return rows

        

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
                


    @staticmethod
    def edit_entry(title,body,entry_id):
        try:
      
            db.cursor.execute("""UPDATE entries  SET title='{}', body='{}' WHERE id='{}' """.format(title,body,entry_id))
            # db.cursor.commit()
        
            return 'entry edited'

        

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    @staticmethod
    def delete_entry(entry_id):
        try:
      
            db.cursor.execute("""DELETE FROM entries WHERE id='{}' """.format(entry_id))
            # db.cursor.commit()
        
            return 'entry deleted succesfully'

        

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


# class RevokedTokenModel():
    
#     def add(self):

    
#     @classmethod
#     def is_jti_blacklisted(cls, jti):



