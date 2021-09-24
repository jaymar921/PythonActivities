import mysql.connector as connectSQL

mySQL = connectSQL.connect(
    host="localhost",
    user="root",
    password="",
    database="firstdatabase"
)

myCursor = mySQL.cursor()

sql = '''SELECT * FROM userdata'''

myCursor.execute(sql)
myResults = myCursor.fetchall()
mySQL.commit()

for result in myResults:
    print(result)