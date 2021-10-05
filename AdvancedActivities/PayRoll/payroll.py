"""
	ABEJAR, JAYHARRON MAR
	BSIT 3
	04549 - IT-ELECPYTHON
"""
from os import system

e_list:list = []
position_list:list = []

#File names
EMPLOYEE_FILE = 'employee.txt'
POSITION_FILE = 'position.txt'
PAYROLL_FILE = 'payroll.txt'

#loadFile module is to load Employees into the list
def loadFile()->None:
	file = open(EMPLOYEE_FILE, "r")
	for item in file:
		e = item.split(',')
		e_list.append(Employee(e[0],e[1],e[2],e[3].split("\n")[0]))
	file1 = open(POSITION_FILE,"r")
	for poss in file1:
		p = poss.split(",")
		position_list.append(Position(p[0],p[1],p[2].split("\n")[0]))
	file.close()
	file1.close()

#save module is to save generated payrolls to payroll.txt
def save(employee:str)->None:
	string = "\n"+employee
	payrolls = open(PAYROLL_FILE,"a")
	payrolls.write(string)
	payrolls.close()

#loadPayrolls module is to load and print the generated payrolls
def loadPayrolls()->None:
	gen = open(PAYROLL_FILE,"r")
	[print(p) for p in gen]

#find module, find the employee in the Employees list
def find():
	system("cls")
	print("Find Employee\n----------------------------\n")
	id = input("IDNO:   ")
	message = "Employee not found!"
	if len(e_list) > 0:
		for employee in e_list:
			if employee.id == id: #If employee is matched, grab the instance
				message = str(employee)
	else: print("There are no employees to display")
	print(message)
	input("Press any key to continue")

#no need comment
def displayall():
	system("cls")
	print("Display All Employees\n----------------------------")
	if len(e_list) > 0:
		for employee in e_list:
			print(employee)
	else: print("There are no employees to display")
	print("----------------------------")
	input("Press any key to continue")

"""
	Ask for user to enter the days of work,
	then multiply the work salary with the days
	After generating the payroll, save it into the
	payroll.txt
"""
def add_number_of_days():
	system("cls")
	print("Add worked days\n----------------------------")
	idno = input("IDNO:   ")
	message = "Employee not found!"

	for employees in e_list:
		if employees.id == idno:
			print(employees)
			day = int(input("Enter day(s) worked: "))
			total = day * float(getPrice(employees.position))
			print(f"Total Salary: {total}")
			e_emp = employees.id+","+employees.firstname+","+employees.firstname+","+getPosition(employees.position)+","+str(total)
			save(e_emp)
			message = "recorded: "+e_emp
			break
	print(message)
	input("Press any key to continue")

#Load the payroll.txt
def generate_payroll():
	system("cls")
	print("Generate Payrolls\n----------------------------")
	loadPayrolls()
	input("Press any key to continue")

"""
	a module ask for position argument, then find scan
	through the positions list, if the position argument
	matches with the position.position, then it returns
	the price or the salary
"""
def getPrice(position:str)->float:
	for pos in position_list:
		if pos.position == position:
			return pos.price
	return 0

"""
	Similar to getPrice module but this will
	return the description of the position
"""
def getPosition(position:str)->str:
	for pos in position_list:
		if pos.position == position:
			return pos.description
	return 'not found'

#Everyone's favorite
def quit()->None:
	print("Program terminated....")

#Display menu module
def display_menu()->None:
	system('cls')
	menu:tuple = (
			"--------- Main Menu ---------",
			"1. Find Employee",
			"2. Display All Employee",
			"3. Add number of day(s) worked",
			"4. Generate Payroll",
			"0. Quit/End"
		)
	[print(x) for x in menu]

#Option selection, using dictionary for accessing
def select(option:int):
	options:dict = {
		1:find,
		2:displayall,
		3:add_number_of_days,
		4:generate_payroll,
		0:quit
	}
	return options.get(option)()

#Classes

class Employee(object):
	def __init__(self, id:str, lastname:str, firstname:str, position:str):
		self.id=id
		self.lastname=lastname
		self.firstname=firstname
		self.position=position
	def __str__(self)->str:
		return f"{self.id}, {self.lastname}, {self.firstname}, {self.position}"

class Position(object):
	def __init__(self, position:str, description:str, price:float):
		self.position=position
		self.description=description
		self.price=price
	def __str__(self)->str:
		return f"{self.position}, {self.description}, {self.price}"






# main
def main():
	loadFile()
	option = -1
	while option != 0:
		display_menu()
		option = int(input("Enter Option(0..4): "))
		select(option)


if __name__ == "__main__":
	main()
