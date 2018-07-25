
from flask import Flask,jsonify,request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

import models, resources


#resources
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/api/v1/entries')



if __name__ == '__main__':
    app.run(debug=True)