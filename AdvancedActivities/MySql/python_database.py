import mysql.connector
from os import system
import json

db = mysql.connector.connect(
	host='127.0.0.1',
	user='root',
	password='',
	database='python_db'
)

def get_all(table:str)->list:
	sql:str=f"SELECT * FROM `{table}`"
	cursor=db.cursor(dictionary=True)
	cursor.execute(sql)
	student_list:list = cursor.fetchall()
	cursor.close()
	return student_list

def add_student(table:str,fields:list=[], data:list=[])->None:
	flds:str = ""
	dta:str=""
	qmark:list=[]
	if len(fields) == len(data):
		[qmark.append("%s") for item in data]
		flds="`,`".join(fields)
		dta="','".join(qmark)
		sql:str=f"INSERT INTO `{table}` (`{flds}`) VALUES ('{dta}')"
		print("QUERY: "+sql+" "+str(tuple(data)))
		


def main()->None:
	system("cls")
	student_list:list = get_all('tbl_student')
	[print(json.dumps(x, indent = 4)) for x in student_list]
	add_student("tbl_student", ['idno','lastname','firstname','course','level'],['0004','ABEJAR','JAYHARRON','BSIT','3'])



if __name__=='__main__':
	main()