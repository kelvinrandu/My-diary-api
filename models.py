# import datetime

# from werkzeug.security import generate_password_hash
# from flask import make_response, jsonify
# from database import DatabaseConnect

# db = DatabaseConnect()

# class User(db.Model):

#     __tablename__ = 'users'
#     id = db.Column(db.Interger, primary_key=True)
#     user_name = db.Column(db.string(250), nullable =False)
#     email = db.Column(db.string(250), nullable =False,unique=True)
#     password = db.Column(db.string(250), nullable =False)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

#     def __repr__(self):
#         return '<user {}>'.format(self.user_name)

#     @classmethod
#     def create_user(cls, username, email, password):
#         """Creates a new user and ensures that the email is unique"""

#         email_results= cls.query.filter_by(email=email).first()

#         if email_results is None:
        
#             return make_response(jsonify({
#                 "message" : "user has been successfully created"
         
#                   }), 201)


#         return make_response(jsonify({"message" : "user with that email already exists"}), 400)
        
# class Entry(db.Model):

#     __tablename__ = 'entries'
#     id = db.Column(db.Interger, primary_key=True)
#     title = db.Column(db.string(250), nullable =False)
#     description = db.Column(db.string(250), nullable =False,unique=True)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

#     def __repr__(self):
#         return '<entry {}>'.format(self.title)