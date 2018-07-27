import datetime

from werkzeug.security import generate_password_hash
from flask import make_response, jsonify
from app import DatabaseConnect

 = DatabaseConnect()

class User(.Model):

    __tablename__ = 'users'
    id = .Column(.Interger, primary_key=True)
    user_name = .Column(.string(250), nullable =False)
    email = .Column(.string(250), nullable =False,unique=True)
    password = .Column(.string(250), nullable =False)
    created_at = .Column(.DateTime, default=datetime.datetime.utcnow)
    updated_at = .Column(.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<user {}>'.format(self.user_name)

    @classmethod
    def create_user(cls, username, email, password):
        """Creates a new user and ensures that the email is unique"""

        email_results= cls.query.filter_by(email=email).first()

        if email_results is None:
        
            return make_response(jsonify({
                "message" : "user has been successfully created"
         
                  }), 201)


        return make_response(jsonify({"message" : "user with that email already exists"}), 400)
        
class Entry(.Model):

    __tablename__ = 'entries'
    id = .Column(.Interger, primary_key=True)
    title = .Column(.string(250), nullable =False)
    description = .Column(.string(250), nullable =False,unique=True)
    created_at = .Column(.DateTime, default=datetime.datetime.utcnow)
    created_at = .Column(.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<entry {}>'.format(self.title)