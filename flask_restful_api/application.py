from flask import Flask
from flask_restful import Api
from rest.employee import Employee
from rest.home import Home

app = Flask(__name__)
api = Api(app)

api.add_resource(Employee, '/employees', '/employees/<employee_id>', methods=['GET'], endpoint='employees')
api.add_resource(Employee, '/employee', methods=['POST'], endpoint='employee')
api.add_resource(Home, '/', methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')