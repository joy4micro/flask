
Flask restful api with MongoDb & Heroku
---

---
The application.py file which is in the main package is basically the entry point to the application and act as a router.
The deployment is done on Heroku. Heroku is a container based cloud Platform as a Service and it is used to deploy, manage, and scale app.
For db, it's connected to the MongoDB Atlas. MongoDB Atlas is the cloud database service. 

---
Steps to run the project on docker locally

    1) docker-compose build
    2) docker-compose up

.env has all the properties for running docker locally

---

To deploy our application on Heroku connecting to a cloud db, we can use the below steps

Steps to setup and run the database server on MongoDb Atlas

    1) we have to create a new cluster
    2) click on Build Cluster
    3) select the shared clusters, create a cluster 
    4) Select any cloud cloud provider and region. (By default, AWS and N. Virginia (us-east-1) are selected).
    Just click on Create cluster 

Once the cluster is created, we can use it.

Please don't add any ip address under 
    
    Network Access -> IP Whitelist -> Add IP Address

We may get, exceptions if we add ip address as shown below

    server selection error: server selection timeout, current topology
    or
    Unknown, rtt: None, error=AutoReconnect

    5) We need to create database by going to

    Collections -> Create Database (say demodb)

    6) We can create collections by going to 

    Collections -> demodb -> Create Collection

---

Once the db setup is done in MongoDb Atlas, we can start deployment in Heroku

Steps to deploy and run the project on heroku

1) to create a project on Heroku, we have 2 options

    a) Create a project on Heroku on the website 

    b) execute the below 2 commands on our terminal (firstly login and then create the project)

        heroku login
        heroku create PROJECT-NAME

2) We have to make sure we set the environment variables in Heroku

        Personal -> Project -> Settings -> Reveal Config Vars 
        Insert KEY and VALUE and click on add

3) Since, it's a docker container project, we have to execute the below command to login to Heroku
heroku container:login  

4) Heroku will build and push the images to the container registry using the below command
heroku container:push web 

5) We can create a new release using
heroku container:release web

6) To open the app in our browser, we can execute
heroku open

7) If anytime we want to see the recent log of the server, we can use 

            heroku logs --tail

---

To test, below are the steps we can follow

1) Post call to http://host-name:5000/employee with the body
    {
    "id": 1,
    "name": "David",
    "address": "USA"
    }
2) Get call to http://host-name:5000/employees to get all the employees
3) Get call to http://host-name:5000/employees/<employee_id> to get only the requested employee details

---

    Locally, on docker, we can use the host-name as localhost, but on heroku, when we do heroku open, it will give us the actual host name, so we can use that


---