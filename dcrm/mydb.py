import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='elvissamoei@2022'
    )

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE.website")

print("ALL DONE!")