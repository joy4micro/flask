from flask import request
from flask_restful import Resource
from employeeRepository import EmployeeRepository


class Employee(Resource):

    def get(self, employee_id=None):
        employee_repository = EmployeeRepository()
        if employee_id is None:
            return employee_repository.find_all()
        else:
            return employee_repository.find(str(employee_id))

    def post(self):
        employee = request.get_json()
        employee_repository = EmployeeRepository()
        return employee_repository.insert_new_employee(str(employee['id']), employee['name'], employee['address'])
