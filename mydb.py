import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'omoregbe=123'
) 


curSorObject = dataBase.cursor()

curSorObject.execute("CREATE DATABASE omos")


print("All done!.")