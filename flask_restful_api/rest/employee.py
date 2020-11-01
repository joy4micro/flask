from flask import request
from flask_restful import Resource

employee_dict = {}


class Employee(Resource):

    def get(self, employee_id=None):
        if employee_id is None:
            return str(employee_dict)
        elif str(employee_id) in employee_dict:
            return str(employee_dict[employee_id])
        return {}

    def post(self):
        employee = request.get_json()
        id = str(employee['id'])
        employee_dict[id] = {'name': employee['name'], 'address': employee['address']}
        return employee

