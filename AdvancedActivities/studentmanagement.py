"""
    Student Management
    
    Jayharron Mar Abejar
    BSIT 3
    04549 IT-ELECTIVE PYTHON PROGRAMMING
"""
from os import system
import Student
from mylist import MyList

LIST=[]
filename = "student.txt"

def updatefile(student:object):
    file = open(filename,"a")
    file.write(str(student)+"\n")
    file.close()
    
def updateall()->None:
    file = open(filename, "w")
    for item in LIST:
        file.write(str(item)+"\n")
    file.close()

def loadfile():
    #clear the list
    LIST.clear()
    file = open(filename,"r")
    for item in file:
        str = item.split()
        LIST.append(Student.Student(str[0],str[1],str[2],str[3],str[4]))
    file.close()


def addstudent():
    system("cls")
    print("------- ADD STUDENT -------")
    idno = input("IDNO      :")
    lastname = input("LASTNAME  :")
    firstname = input("FIRSTNAME :")
    course = input("COURSE    :")
    level = input("LEVEL     :")
    # do not allow un-filled input
    message = "\nFill all fields"
    if idno!="" and lastname != "" and firstname != "" and course != "" and level != "":
        stud = Student.Student(idno,lastname,firstname,course,level)
        LIST.append(stud)
        message = "new Student Added"
        updatefile(stud)
    print(message)
    input("Press Enter key to continue")
    
    
def findstudent():
    loadfile()
    system("cls")
    print("------- FIND STUDENT -------")
    idno = input("Find Student by IDNO: ")
    message = "Student not found"
    if len(LIST) > 0:
        for item in LIST:
            if item.__eq__(idno):
                message = "Found - "+str(item)
                break
    print(message)
    input("Press any key to continue")
    
    
def deletestudent()->None:
    loadfile()
    system("cls")
    print("------- DELETE STUDENT -------")
    idno = input("Find Student by IDNO: ")
    message = "Student not found"
    if len(LIST)>0:
        for item in LIST:
            if item.__eq__(idno):
                print(item)
                confirm = input("Do you want to delete this student(y/n): ")
                if confirm == "y":
                    LIST.remove(item)
                    message = "\nStudent was removed"
                    updateall()
    print(message)
    input("Press any key to continue...")
    
def updatestudent()->None:
    loadfile()
    system("cls")
    print("------- DELETE STUDENT -------")
    idno = input("Find Student by IDNO: ")
    message = "Student not found"
    if len(LIST)>0:
        for item in LIST:
            if item.__eq__(idno):
                index = LIST.index(item)
                print(item)
                confirm = input("Do you want to update this student(y/n): ")
                if confirm == "y":
                    print("IDNO      :"+idno)
                    lastname = input("LASTNAME  :")
                    firstname = input("FIRSTNAME :")
                    course = input("COURSE    :")
                    level = input("LEVEL     :")
                    # do not allow un-filled input
                    message = "\nFill all fields"
                    if lastname != "" and firstname != "" and course != "" and level != "":
                        stud = Student.Student(idno,lastname,firstname,course,level)
                        LIST[index] = stud
                        message = "\nStudent updated"
                        updateall()
    print(message)
    input("Press any key to continue")
    
def displayall():
    system("cls")
    print("------- STUDENT LIST -------")
    loadfile()
    if len(LIST) > 0:
        [print(item) for item in LIST]
    else:
        print("\nList is Empty")
    input("Press Enter key to continue")
    
def quit():print("Program Terminated...")

def get_option(option:int):
    menuoptions={
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:updatestudent,
        5:displayall,
        0:quit,
    }
    return menuoptions.get(option)()

def displaymenu():
    system("cls")
    menuitems = (
        "-------- Main Menu --------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/End",
    )
    [print(item) for item in menuitems]
    

def main():
    option = -1
    while option != 0:
        displaymenu()
        option=int(input("Enter Option(0..5): "))
        get_option(option)


if __name__ == "__main__":
    main()