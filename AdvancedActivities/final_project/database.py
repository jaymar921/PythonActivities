from mysql import connector

#Connect to database
DATABASE = connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = 'python_employee'
)


def SAVE_DB(data:dict)->int:
	flag:str = data.get("flag")
	idno:str = data.get("idno")
	lastname:str = data.get("lastname")
	firstname:str = data.get('firstname')
	course:str = data.get("course")
	level:str = data.get("level")
	try:
		sql:str = ""
		if '-' in flag:
			sql = f"INSERT INTO `student` (`idno`,`lastname`,`firstname`,`course`,`level`) VALUE ('{idno}','{lastname}','{firstname}','{course}','{level}')"
		else:
			sql = f"UPDATE `student` SET idno='{idno}',lastname='{lastname}',firstname='{firstname}',course='{course}',level='{level}' WHERE id='{flag}'"
		cursor = DATABASE.cursor()
		cursor.execute(sql)
		DATABASE.commit()
		cursor.close()	
	except Exception:
		return 1 # Error if return code 1
	if '-' in flag:
		return 0 # New Student added if return code 0
	else:
		return 2 # Update Student if return code 2

def DELETE_STUDENT(idno:int):
	try:
		sql:str = f"DELETE FROM `student` WHERE `id`={idno}"
		cursor = DATABASE.cursor()
		cursor.execute(sql)
		DATABASE.commit()
		cursor.close()
	except Exception:
		return False
	return True

def GETALL()->list:
	sql:str = f"SELECT * FROM `student`"
	cursor = DATABASE.cursor(dictionary=True)
	cursor.execute(sql)
	slist:list = cursor.fetchall()
	cursor.close()
	return slist

def ValidateUser(username:str,password:str)->bool:
	sql:str = f"SELECT * FROM `user` WHERE `username`='{username}' and `password`='{password}'"
	cursor = DATABASE.cursor()
	cursor.execute(sql)
	slist:list = cursor.fetchall()
	cursor.close()
	return len(slist)>0

def GET_ALL()->list:
	sql:str = f"select employee.id,employee.idno,employee.lastname,employee.firstname,position.position_desc,position.daily_rate from `employee` inner join position on employee.position_code = position.position_code"
	cursor = DATABASE.cursor(dictionary=True)
	cursor.execute(sql)
	elist:list = cursor.fetchall()
	cursor.close()
	return elist

def GET_PAYROLL()->list:
	sql:str = f"select * from payroll"
	cursor = DATABASE.cursor(dictionary=True)
	cursor.execute(sql)
	elist:list = cursor.fetchall()
	cursor.close()
	return elist

def SAVE_PAYROLL(data:dict)->int:
	idno:str = data.get('idno')
	name:str = data.get('name')
	rate:str = data.get('rate')
	date_from:str = data.get('date_from')
	date_to:str = data.get('date_to')
	days:str = data.get('days')
	salary:str = data.get('salary')[1:]

	if len(salary.split(',')) == 2:
		salary = salary.split(',')[0] + salary.split(',')[1]
	try:
		sql:str = f"insert into `payroll` (`idno`,`name`,`daily_rate`,`date_from`,`date_to`,`days`,`salary`) value ('{idno}','{name}','{rate}','{date_from}','{date_to}',{days},{float(salary)})"
		cursor = DATABASE.cursor()
		cursor.execute(sql)
		DATABASE.commit()
		cursor.close()
	except:
		return 1
	return 0

def DELETE_PAYROLL(idno:int):
	try:
		sql:str = f"DELETE FROM `payroll` WHERE `id`={idno}"
		cursor = DATABASE.cursor()
		cursor.execute(sql)
		DATABASE.commit()
		cursor.close()
	except Exception:
		return False
	return True

def formatter(amount:float)->str:
	return "₱{:,.2f}".format(amount)