import os
from pymongo import MongoClient

HOST_NAME=os.environ.get("HOST_NAME")
DB_USERNAME=os.environ.get("DB_USERNAME")
PASSWORD=os.environ.get("PASSWORD")
DATABASE_NAME=os.environ.get("DATABASE_NAME")
PROD_ENVIRON=os.environ.get("PROD_ENV")


class DatabaseConfig:

    def getDbClient(self):

        if PROD_ENVIRON == 'True':
            return MongoClient("mongodb+srv://"+DB_USERNAME+":"+PASSWORD+"@"+HOST_NAME+"/"+DATABASE_NAME+"?retryWrites=true&w=majority")
        else:
            return MongoClient(host=HOST_NAME,
                        port=27017,
                        username=DB_USERNAME,
                        password=PASSWORD,
                        authSource="admin")
            #return MongoClient("mongodb+srv://"+DB_USERNAME+":"+PASSWORD+"@"+HOST_NAME+"/"+DATABASE_NAME+"?authSource=admin")   


    def getDatabaseName(self):
        return os.environ.get("DATABASE_NAME")