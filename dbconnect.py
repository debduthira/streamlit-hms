import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    port="3306",
    user="debdut",
    password="GUDDUdebdut007",
    database="hmsystem"
)

mycursor = mydb.cursor()
