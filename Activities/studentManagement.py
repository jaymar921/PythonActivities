""""
    Abejar, Jayharron Mar 
    BSIT 3
    04549 IT-ELPYTHON
    9:00-11:30 TTH
    
    Student Management
"""
from os import system
import student

student_list=[]

def addstudent():
    print("Add Student")
    print("----------------")
    idno = input("IDNO     : ")
    lastname = input("LASTNAME : ")
    firstname = input("FIRSTNAME: ")
    course = input("COURSE   : ")
    level = input("LEVEL    : ")
    #input validation
    if idno != "" and lastname != "" and firstname !="" and course != "" and level != "":
        student_list.append(student.Student(idno,lastname, firstname, course, level))
        print("New Student Added")
    else:
        print("Fill all fields")
    input("Press any key to continue")
    
def findstudent():
    print("Find Student")
    print("-------------")
    idno = input("Find Student by IDNO: ")
    message = "Student not found"
    for student in student_list:
        if student.__eq__(idno):
            message = student.__str__()
            break;
    print(message)
    input("Press any key to continue")
    
def deletestudent(): 
    print("Delete Student")
    print("-------------")
    idno = input("Delete Student by IDNO: ")
    message = "Student not found"
    for student in student_list:
        if student.__eq__(idno):
            message = "Successfully deleted \nstudent --> "+student.__str__()
            student_list.remove(student)
            break;
    print(message)
    input("Press any key to continue")
    
def updatestudent(): 
    print("Update Student")
    print("--------------")
    idno = input('Find student by IDNO: ')
    message = "Student not found"
    for students in student_list:
        if students.__eq__(idno):
            print("Record Found: "+students.__str__())
            lastname = input("LASTNAME : ")
            firstname = input("FIRSTNAME: ")
            course = input("COURSE   : ")
            level = input("LEVEL    : ")
            if idno != "" and lastname != "" and firstname !="" and course != "" and level != "":
                student_list.remove(students)
                st_new = student.Student(idno, lastname, firstname, course, level)
                student_list.append(st_new)
                message = "Successfully updated \nstudent --> "+students.__str__()+"\nto      --> "+st_new.__str__()
            else:
                message = "Fill all the fields | Update was unsuccessful"
            break;
    print(message)
    input("Press any key to continue")
    
def displayAllstudent(): 
    print("Display All Students")
    print("--------------------")
    [print(student) for student in student_list]
    input("Press Any Key To Continue")
def quit(): print("Program Terminated...")

def displayMenu():
    system("cls")
    menuitems=(
        "----- Main Menu -----",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/End",
    )
    [print(x) for x in menuitems]

def get_option(option):
    menufunctions={
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:updatestudent,
        5:displayAllstudent,
        0:quit,
    }
    return menufunctions.get(option)()

def main():
    option = -1
    while option != 0:
        displayMenu()
        #try:
        option = int(input("Enter option(0..5): "))
        get_option(option)
        #except Exception:
        #    print("Invalid Option")
        #    input("Press any key to continue")

if __name__=="__main__":
    main()
