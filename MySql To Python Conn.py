import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='power'
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE power")

#mycursor.execute("SHOW DATABASES")
# for i in mycursor:
# print(i)

#mycursor.execute("CREATE TABLE DATA(name VARCHAR(255),address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")
# for i in mycursor:
# print(i)

#sql="INSERT INTO DATA(name,address)VALUES(%s,%s)"
# val=("durga","hyd")
# mycursor.execute(sql,val)

sql = "UPDATE DATA SET address='bhimavaram' WHERE address='hyd'"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("SELECT * FROM DATA")
result = mycursor.fetchall()
for i in result:
    print(i)
