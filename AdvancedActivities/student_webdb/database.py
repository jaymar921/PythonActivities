from mysql import connector

#Connect to database
DATABASE = connector.connect(
    host = "192.168.1.122",
    user = "root",
    password = "",
    database = 'pythontth'
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

