from pymongo import MongoClient
import json

HOST_NAME = "empdb"
PORT = 27017
DATABASE_NAME = 'employeedb'
TABLE_NAME = 'employee'

#client = MongoClient(host=HOST_NAME, port=PORT, authSource='admin')
client = MongoClient("mongodb://empdb:27017")
employee_db = client[DATABASE_NAME]
employee_collection = employee_db[TABLE_NAME]


class EmployeeRepository:

    def insert_new_employee(self, id, name, address):
        employee = {'id': str(id), 'name': name, 'address': address}
        inserted_employee = employee_collection.insert_one(employee)
        return 'inserted' if inserted_employee.acknowledged else 'not inserted' 

    def find(self, id):
        find_by_id = {'id': str(id)}
        result = employee_collection.find_one(find_by_id)
        for record in result: 
            print(" >>>>> ", record, flush = True)
        return "find one only"

    def find_all(self):
        find_by_id = {'id': 1}
        return employee_collection.find(find_by_id)
