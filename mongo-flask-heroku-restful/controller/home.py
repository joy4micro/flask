from flask_restful import Resource
from flask_cors import CORS,cross_origin


class Home(Resource):

    @cross_origin()
    def get(self):
        return 'flask restful api, version: 1.0.0'

