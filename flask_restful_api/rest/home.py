from flask_restful import Resource


class Home(Resource):

    def get(self):
        return 'flask restful api, version: 1.0.0'

