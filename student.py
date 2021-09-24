"""
    Student Class
"""

class Person(object):
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    
    def __str__(self):
        return f"{self.lastname} {self.firstname}"
    
    def __eq__(self, other):
        return self.lastname==other.lastname and self.firstname == other.firstname

######################################################
class Student(Person):
    
    def __init__(self, idno, lastname, firstname, course, level):
        super().__init__(lastname, firstname);
        self.idno = idno
        self.course = course
        self.level = level
        
    def __str__(self):
        return f"{self.idno} {super().__str__()} {self.course} {self.level}"
        
    def __eq__(self, other):
        return self.idno == other.idno
        
    def __eq__(self, idno):
        return self.idno == idno;
    
s1 = Student("0001", "Abejar","Jayharron","BSIT","3")
print(s1)