"""
	Student Class
"""

class Person(object): #Parent Class

	def __init__(self, lastname, firstname): #Person Class Constructor
		self.lastname = lastname
		self.firstname = firstname

	def __eq__(self, other):
		if self is other: return True
		if type(self) != type(other): return False
		return self.lastname==other.lastname and self.firstname == other.firstname

	def __str__(self):
		return f"{self.lastname} {self.firstname}"


class Student(Person): #Sub Class

	def __init__(self, idno:str, lastname:str, firstname:str, course:str, level:str):#Student Class Constructor
		super().__init__(lastname, firstname) #Initialize the Parent Class Constructor
		self.idno = idno
		self.course = course
		self.level = level

	def __eq__(self, other:object): #Equal module
		if self is other: return True
		if type(self) != type(other): return False
		return self.idno == other.idno

	def __eq__(self, idno:str): #Equal module
		return self.idno == idno

	def __str__(self): #toString Module
		return f"{self.idno} {super().__str__()} {self.course} {self.level}"


#p1 = Student("001", "Abejar","Jayharron Mar","BSIT","4")
#print(p1)