---

It's a flask restful api project. Every python file in the rest package has its own responsibility.
The application.py file which is in the main package is basically the entry point to the application and act as a router

Steps to run the project on docker

1) docker-compose build
2) docker-compose up

By default, the server is WSGI

---

To test, below are the steps we can follow

1) Post call to http://localhost:5000/employee with the body
    {
    "id": 1,
    "name": "David",
    "address": "USA"
    }
2) Get call to http://localhost:5000/employees to get all the employees
3) Get call to http://localhost:5000/employees/<employee_id> to get only the requested employee details
---