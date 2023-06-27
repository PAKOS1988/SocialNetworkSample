
from flask_restx import Resource, Api
from flask import Blueprint
from database.userservice import register_user_db, get_exact_user_db, get_all_users_db

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
api=Api(swagger_bp)
#Первый тестовый интерфейс для тестов
@api.route('/test-swag')
class TestSwagger(Resource):
    #Метод HTTP
    def get(self):
        return {'message':"Swagger is working"}
@api.route('/test-user')
class TestUserSwagger(Resource):
    #Метод HTTP
    def get(self):
        all_users = get_all_users_db()
        return {'message':all_users}

