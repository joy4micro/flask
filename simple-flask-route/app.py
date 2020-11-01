from flask import Flask, request

app = Flask(__name__)

employee_dict = {}


@app.route('/')
def welcome():
    return 'Welcome!'


@app.route('/employee')
def employee():
    return str(employee_dict)


@app.route('/employee')
def employee():
    print(request.get_json())
    return str(employee_dict)


@app.route('/employee', methods=['POST'])
def new_employee():
    employee = request.get_json()
    id = employee['id']
    employee_dict[id] = {'name': employee['name'], 'address': employee['address']}
    return employee


if __name__ == '__main__':
    app.run(debug=True)