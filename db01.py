import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="runoob_db"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM sites WHERE name ='RUNOOB'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)