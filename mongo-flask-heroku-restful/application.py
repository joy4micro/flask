import flask
import flask_restful

from home import Home
from employee import Employee

app = flask.Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(Employee, '/employees', '/employees/<employee_id>', methods=['GET'], endpoint='employees')
api.add_resource(Employee, '/employee', methods=['POST'], endpoint='employee')
api.add_resource(Home, '/', methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')