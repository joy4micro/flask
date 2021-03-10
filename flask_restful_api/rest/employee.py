from flask import request
from flask_restful import Resource
from employeeRepository import EmployeeRepository


class Employee(Resource):

    def get(self, employee_id=None):
        employeeRepository = EmployeeRepository()
        if employee_id is None:
            return employeeRepository.find_all()
        else:
            return employeeRepository.find(str(employee_id))

    def post(self):
        employee = request.get_json()
        employeeRepository = EmployeeRepository()
        return employeeRepository.insert_new_employee(str(employee['id']), employee['name'], employee['address'])