from flask import jsonify
from databaseConfig import DatabaseConfig

TABLE_NAME = 'employee'

class EmployeeRepository:

    config = DatabaseConfig()
    client = config.getDbClient()
    employee_db = client[config.getDatabaseName()]
    employee_collection = employee_db[TABLE_NAME]

    def insert_new_employee(self, id, name, address):
        try:
            employee = {'id': str(id), 'name': name, 'address': address}
            inserted_employee = self.employee_collection.insert_one(employee)
            return 'inserted' if inserted_employee.acknowledged else 'not inserted'
        except:
            pass
        finally:
            if type(employee_db) == client:
                employee_db.close()

    def find(self, id):
        find_by_id = {'id': str(id)}
        result = self.employee_collection.find_one(find_by_id)
        del result['_id']
        return jsonify(result)

    def find_all(self):
        employees = self.employee_collection.find()
        employees_json = [{'id': employee['id'], 'name': employee['name'], 'address': employee['address']} for employee in employees]
        return jsonify({'employees': employees_json})