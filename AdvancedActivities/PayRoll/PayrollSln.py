"""
	PayRoll solution by sir dennis
"""
from os import system

position_list = []
employee_list = []

def load_position()->None:
	file = open("position.txt")
	position = {}
	for line in file:
		value = line.split(",") #return a list of data of every line in position
		position["code"] = value[0]
		position["position"] = value[1]
		position["daily_rate"] = value[2].strip("\n")
		position_list.append(dict(position))
	return

def load_employee()->None:
	load_position()
	file = open("employee.txt")
	employee = {}
	for line in file:
		value=line.split(",")
		employee["idno"]=value[0]
		employee["lastname"]=value[1]
		employee["firstname"]=value[2]
		for pos in position_list:
			if pos["code"] == str(value[3]).strip("\n"):
				employee["position"] = pos["position"]
				employee["daily_rate"] = pos["daily_rate"]
				employee_list.append(dict(employee))
	#print(employee_list)
	return

def find_employee()->None:
	system("cls")
	idno:str = input("Find Employee by id: ")
	for emp in employee_list:
		if emp["idno"] == idno:
			print(f"{emp['idno']} {emp['lastname']} {emp['firstname']} {emp['position']} {emp['daily_rate']}")
	return

def display_all()->None:
	for emp in employee_list:
		print(f"{emp['idno']} {emp['lastname']} {emp['firstname']} {emp['position']} {emp['daily_rate']}")
	return

def add_days_worked()->None:
	file = open("payroll.txt","a")
	system("cls")
	idno:str = input("Enter idno:")
	for emp in employee_list:
		if emp["idno"] == idno:
			print(f"{emp['idno']} {emp['lastname']} {emp['firstname']} {emp['position']} {emp['daily_rate']}")
			days_worked:int = int(input("Enter days worked: "))
			total_salary:float = days_worked * float(emp['daily_rate'])
			print("Total Salary: "+str(total_salary))
			data = f"\n{emp['idno']},{emp['lastname']},{emp['firstname']},{emp['position']},{str(total_salary)}"
			file.write(str(data))
	return

def generate_payroll()->None:
	file = open("payroll.txt", "r")
	try:
		[print(payroll) for payroll in file]
	except Exception:
		print("No payroll generated")
	return

def quit()->None:
	print("Program terminated...")

def display_menu()->None:
	system("cls")
	menuitems:tuple = (
			"----- Main Menu -----",
			"1. Find Employee",
			"2. Display all Employee",
			"3. Add number of days worked",
			"4. Generate Payroll",
			"---------------------"
		)
	[print(item) for item in menuitems]



def get_option(option:int)->None:
	menuoption:dict = {
		1:find_employee,
		2:display_all,
		3:add_days_worked,
		4:generate_payroll,
		0:quit
	}
	return menuoption.get(option)()

def main() -> None:
	load_employee()
	option:int = -1
	while option != 0:
		display_menu()
		option = int(input("Enter Option (0..4): "))
		get_option(option)
		input("Press any key to continue...")
	

if __name__=='__main__':
	main()