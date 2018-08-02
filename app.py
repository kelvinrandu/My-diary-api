
from flask import Flask, jsonify,request
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)


app.config['JWT_SECRET_KEY'] = 'ghasfksfgksrhskh',
app.config['JWT_BLACKLIST_ENABLED'] = True ,
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

jwt = JWTManager(app)

# resources
import  models, resources

api.add_resource(resources.UserRegistration, '/api/v1/register')
api.add_resource(resources.UserLogin, '/api/v1/login')
api.add_resource(resources.UserLogoutAccess, '/api/v1/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/api/v1/logout/refresh')
api.add_resource(resources.TokenRefresh, '/api/v1/token/refresh')
api.add_resource(resources.SecretResource, '/api/v1/secret')
api.add_resource(resources.AllEntries, '/api/v1/entries')
api.add_resource(resources.EachEntry, '/api/v1/entries/<int:id>')
api.add_resource(resources.PostEntry, '/api/v1/entries')
api.add_resource(resources.EditEntry, '/api/v1/entries/<int:id>')
api.add_resource(resources.DeleteEntry, '/api/v1/entries/<int:id>')



if __name__ == '__main__':
    app.run(debug=True)