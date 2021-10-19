"""
	Student Database
	Establish a connection from this application to
	MySQL database server
"""
import mysql.connector as sql
import json
from os import system

db = sql.connect(
		host = "127.0.0.1",
		user="root",
		password="",
		database = "python_db"
	)

def get_all(table:str)->list:
	query:str = f"SELECT * FROM `{table}`"
	connection = db.cursor(dictionary=True)
	connection.execute(query) 
	return connection.fetchall()

#Add data into the database
def add_item(table:str,fields:list=[],data:list=[])->bool:
	#INSERT INTO `table` (`fld1`,`fld2`,`fld3`,`fld4`,`fld5`) VALUES (%s,%s,%s,...)
	qmark:list = []
	okey:bool = False
	if len(fields) == len(data):
		[qmark.append("%s") for item in data] #populate the qmark list
		flds:str="`,`".join(fields)
		dta:str=",".join(qmark)
		query = f"INSERT INTO `{table}` (`{flds}`) VALUES ({dta})"
		print(query)
		connection = db.cursor()
		connection.execute(query,data)
		db.commit()
		connection.close()
		okey = True
	return okey

def update_item(table:str,id:int,fields:list=[],new_data:list=[])->bool:
	#UPDATE `table` SET `fld1`=%s, `fld2`=%s, `fld3`=%s WHERE `id`=%s
	okey:bool = False

	if len(fields) == len(new_data):
		flds:str="`=%s,`".join(fields)
		flds+="`=%s"
		query:str=f"UPDATE `{table}` SET `{flds} WHERE `id`={id}"
		print(query)
		connection = db.cursor()
		connection.execute(query,new_data)
		db.commit()
		connection.close()
		okey = True
	return okey

def delete_item(table:str,id:int)->bool:
	query:str = f"DELETE FROM {table} WHERE id={id}" 
	okay:bool = False
	print(query)
	try:
		connection = db.cursor()
		connection.execute(query)
		db.commit()
		connection.close()
		okay = True
	except Exception:
		print("Error deleting the record")
	return okay;

def find_item(table:str,id:int)->list: 
	query:str = f"SELECT * FROM `{table}` WHERE `id`={id}"
	connection = db.cursor(dictionary=True)
	connection.execute(query) 
	return connection.fetchall()[0]



def main()->None:
	system("cls")
	#print("student_list:"+json.dumps(get_all("tbl_student"), indent=4))
	#status:bool = add_item("tbl_student",['idno','lastname','firstname','course','level'],['0004','SAMPLE','USER','BSEE','2'])
	#print(status)
	#status:bool = update_item("tbl_student",5,['idno','lastname','firstname','course','level'],['0004','USER','SAMPLE','BSME','3'])
	#print(delete_item("tbl_student",5))
	print(json.dumps(find_item("tbl_student", 1), indent=4))

if __name__=='__main__':
	main()