
from flask_restx import Resource, Api
from flask import Blueprint

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
api=Api(swagger_bp)
#Первый тестовый интерфейс для тестов
@api.route('/test-swag')
class TestSwagger(Resource):
    #Метод HTTP
    def get(self):
        return {'message':"Swagger is working"}