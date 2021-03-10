from flask import jsonify
from pymongo import MongoClient

HOST_NAME = 'mongodb'
PORT = 27017
DATABASE_NAME = 'empdb'
TABLE_NAME = 'employee'
USERNAME = 'root'
PASSWORD = 'pass'

dbClient = MongoClient(host=HOST_NAME,
                       port=PORT,
                       username=USERNAME,
                       password=PASSWORD,
                       authSource="admin")
employee_db = dbClient[DATABASE_NAME]
employee_collection = employee_db[TABLE_NAME]


class EmployeeRepository:

    def insert_new_employee(self, id, name, address):
        try:
            employee = {'id': str(id), 'name': name, 'address': address}
            inserted_employee = employee_collection.insert_one(employee)
            return 'inserted' if inserted_employee.acknowledged else 'not inserted'
        except:
            pass
        finally:
            if type(employee_db) == MongoClient:
                employee_db.close()

    def find(self, id):
        find_by_id = {'id': str(id)}
        result = employee_collection.find_one(find_by_id)
        del result['_id']
        return jsonify(result)

    def find_all(self):
        employees = employee_collection.find()
        employees_json = [{'id': employee['id'], 'name': employee['name'], 'address': employee['address']} for employee in employees]
        return jsonify({'employees': employees_json})