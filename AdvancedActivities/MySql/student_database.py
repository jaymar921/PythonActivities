'''
	STUDENT DATABASE
	BY: JAYHARRON MAR ABEJAR
	PYTHON-ELECTIVE 04549
	TTH 10:30 TO 11:30 AM

	Database name: pythontth
	table: student
		attributes:

		id -> int, pk, auto increment
		idno -> varchar(10)
		lastname -> varchar(50)
		firstname -> varchar(50)
		course -> varchar(10)
		level -> varchar(5)
'''
import mysql.connector as mysql
import json
from os import system

database = mysql.connect(
		host="127.0.0.1",
		user="root",
		password="",
		database="pythontth"
	)
db_table = "student"


mymenu:list = [
		"------------ [ STUDENT DATABASE ] ------------",
		"  DATABASE: pythontth        STUDENTS:",
		"----------------------------------------------",
		" 1. Find Student",
		" 2. Add Student",
		" 3. Update Student",
		" 4. Delete Student",
		" 5. Display All Student",
		" 0. Exit Program",
		"----------------------------------------------"
	]

def sql_query(option:str, data:list=[])->list:
	fields:list = ['idno','lastname','firstname','course','level']
	query:str = ""
	smark:list=[]
	out:list=[]
	if "insert" in option:
		[smark.append("%s") for x in range(len(data))]
		field:str = "`,`".join(fields)
		_data:str = ",".join(smark)
		query = f"INSERT INTO `{db_table}` (`{field}`) VALUES ({_data})"
	elif "find" in option:
		query = f"SELECT * FROM `{db_table}` WHERE `id`={data[0]}"
	elif "all" in option:
		query = f"SELECT * FROM `{db_table}`"
	elif "update" in option:
		field:str="`=%s,`".join(fields)
		field+="`=%s"
		query = f"UPDATE `{db_table}` SET `{field} WHERE id={data[0]}"
	elif "delete" in option:
		query = f"DELETE FROM `{db_table}` WHERE id={data[0]}"

	#print(query)
	try:
		cursor = database.cursor()
		if "insert" in option:
			cursor.execute(query,data)
			out.append("Query Success")
		elif "update" in option:
			new_data:list = [data[1],data[2],data[3],data[4],data[5]]
			cursor.execute(query,new_data)
			out.append("Update Query Success")
		elif "find" in option or "all" in option:
			cursor.execute(query)
			out:list = cursor.fetchall()
		elif "delete" in option:
			cursor.execute(query)
			out.append("Delete Success")
		database.commit()
	except Exception:
		print(":: There was a query issue")
		out.append("Database issue")
	finally:
		cursor.close()
		
	return out

def format_tuple(data:tuple, option:str)->None:
	if "vertical" in option.lower():
		print("ID         : "+str(data[0]))
		print("ID NUMBER  : "+str(data[1]))
		print("LASTNAME   : "+str(data[2]))
		print("FIRSTNAME  : "+str(data[3]))
		print("COURSE     : "+str(data[4]))
		print("LEVEL      : "+str(data[5]))
	if "horizontal" in option.lower():
		print(f"  {str(data[0]):5} | {str(data[1]):5} | {str(data[2]):15} | {str(data[3]):20} | {str(data[4]):6} | {str(data[5]):6}|")
			

def verification(i:str,l:str,f:str,c:str,lvl:str)->bool:
	return i!="" and l!="" and f!= "" and c!="" and lvl!=""

def confirmation()->bool:
	confirmation:str = input("CONFIRM(Y/N)    : ")
	confirmation = confirmation.lower()
	if confirmation == 'y':
		print(":: Process was confirmed")
		return True
	elif confirmation == 'n':
		print(":: Process was declined")
		return False
	else:
		print("Invalid input... `n` option was selected")

def update_student_format(data:tuple)->None:
	print(f"ID              : {data[0]: < 10} ")
	idno:str = input(f"ID NUMBER       : [{data[1]:10}] ")
	lastname:str = input(f"LASTNAME        : [{data[2]:10}] ")
	firstname:str = input(f"FIRSTNAME       : [{data[3]:10}] ")
	course:str = input(f"COURSE          : [{data[4]:10}] ")
	level:str = input(f"LEVEL           : [{data[5]:10}] ")
	message = ""
	if not verification(idno, lastname, firstname, course, level):
		message = ":: You have to fill all the fields"
	else:
		print(":: Are you sure you want to append the data\ninto the student table in pythontth")
		if confirmation():
			out:list=sql_query("update",[data[0],idno,lastname,firstname,course,level])
			message = f":: Student {idno} has been updated into the database ["+out[0]+"]"
			if "issue" in out[0]:
				message = f":: Failed to update student {idno}..."
	print(message)

def find_student()->None:
	print("---------- [ ADD STUDENT DATABASE ] ----------")
	idno:str = input("ID NUMBER       : ")
	out:list = sql_query("find",[idno])
	print(":: SEARCHING STUDENT QUERY\n")
	if len(out)==1:
		print("Record Found:")
		format_tuple(out[0],"vertical")
		print("------------ [ SEARCH COMPLETED ] ------------")
	else:
		print("Nothing Found:\n")
		print("------------ [ SEARCH COMPLETED ] ------------")

def add_student()->None:
	print("---------- [ ADD STUDENT DATABASE ] ----------")
	idno:str = input("ID NUMBER       : ")
	lastname:str = input("LASTNAME        : ")
	firstname:str = input("FIRSTNAME       : ")
	course:str = input("COURSE          : ")
	level:str = input("LEVEL           : ")
	message = ""
	if not verification(idno, lastname, firstname, course, level):
		message = ":: You have to fill all the fields"
	else:
		print(":: Are you sure you want to append the data\ninto the student table in pythontth")
		if confirmation():
			out:list=sql_query("insert",[idno,lastname,firstname,course,level])
			message = f":: Student {idno} has been added into the database ["+out[0]+"]"
			if "issue" in out[0]:
				message = f":: Failed to add student {idno}..."
		

	print(message)


def update_student()->None:
	print("-------- [ UPDATE STUDENTS DATABASE ] --------")
	student_id:str = input("ID NUMBER       : ")
	out:list = sql_query("find",[student_id])
	print(":: SEARCHING STUDENT QUERY\n")
	if len(out)==1:
		print("Record Found:")
		format_tuple(out[0],"h")
		print("------------- [ UPDATE STUDENT ] -------------")
		update_student_format(out[0])
	else:
		print("Nothing Found:\n")
		print("------------ [ SEARCH COMPLETED ] ------------")
		return

def delete_student()->None:
	print("-------- [ DELETE STUDENTS DATABASE ] --------")
	idno:str = input("ID NUMBER       : ")
	out:list = sql_query("find",[idno])
	print(":: SEARCHING STUDENT QUERY\n")
	if len(out)==1:
		print("Record Found:")
		format_tuple(out[0],"h")
		print("------------ [ SEARCH COMPLETED ] ------------")
		print(":: Are you sure you want to delete the data\nfrom the student table in pythontth")
		if confirmation():
			out:list=sql_query("delete",[idno])
			print(":: status: ["+str(out[0])+"]")

	else:
		print("Nothing Found:\n")
		print("------------ [ SEARCH COMPLETED ] ------------")
		return

def display_student()->None:
	print("------------ [ DISPLAY STUDENTS ] ------------")
	out:list = sql_query("all",[])
	print("Records found: ")
	print("___________________________________________________________________________")
	print("  ID    | ID NO |   LASTNAME      |       FIRSTNAME      | COURSE | LEVEL |")
	print("‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾|")
	if len(out) >0:
		for data in out:
			format_tuple(data,"horizontal")
	else:
		format_tuple(("--","--","-----","-----","----","-"),"horizontal")
	format_tuple((" "," "," "," "," "," "),"horizontal") #For display purpose hehehee
	print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")
def quit()->None:
	print("Program Terminated...")

def rows()->str:
	try:
		query = f"SELECT * FROM `{db_table}`"
		cursor = database.cursor()
		cursor.execute(query)
		rows = len(cursor.fetchall())
		cursor.close()
	except Exception:
		return "Expired Session"
	return str(rows)


def get_option(option:int):
	option_dict:dict={
		1:find_student,
		2:add_student,
		3:update_student,
		4:delete_student,
		5:display_student,
		0:quit
	}
	return option_dict[option]()

def display_menu()->None:
	system("cls")
	mymenu[1] = "  DATABASE: pythontth        STUDENTS:"+rows()
	[print(x) for x in mymenu]

def main():
	option:int = -1
	while option != 0:
		display_menu()
		try:
			option = int(input("Enter Option (0...5): "))
			get_option(option)
		except Exception as e:
			option = 10
			print("Invalid input...")
		input("Press any key to continue...")



if __name__=='__main__':
	main()