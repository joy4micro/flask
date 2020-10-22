from flask import Flask

''' create a Flask application using the Flask app factory pattern'''
def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        ''' render a Hello world response, return flask response '''
        return 'Hello from skeleton!'

    return app

