from flask import request
from flask_restful import Resource
from employeeRepository import EmployeeRepository
from flask_cors import CORS,cross_origin


class Employee(Resource):

    @cross_origin()
    def get(self, employee_id=None):
        employee_repository = EmployeeRepository()
        if employee_id is None:
            return employee_repository.find_all()
        else:
            return employee_repository.find(str(employee_id))

    @cross_origin()
    def post(self):
        employee = request.get_json()
        employee_repository = EmployeeRepository()
        return employee_repository.insert_new_employee(str(employee['id']), employee['name'], employee['address'])
