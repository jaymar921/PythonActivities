"""
    Updated Student Management System
    
    Jayharron Mar Abejar
    BSIT 3
    04549 IT-ELECTIVE PYTHON PROGRAMMING

"""
from os import system
from mylist import MyList
from Student import Student

#NAME OF THE FILE TO STORE THE LIST
FILENAME = "studentlist.txt"

#DATASTRUCTURE, creating StudentList from MyList class (Java ways)
#       same as 'StudentList<Student> slist = new StudentList<>();'
StudentList:MyList = MyList()

#SAVING LISTED STUDENTS INTO A FILE
#From memory data to permanent data
def save_list()->None:
    students = StudentList.get_list()
    file = open(FILENAME, "w")
    for student in students:
        file.writelines(str(student)+"\n")
    file.close()

#LOADING DATA FROM FILE TO MEMORY
def load_list()->None:
    StudentList.get_list().clear() #CLEARING StudentList
    try:
        file = open(FILENAME, "r")
        for student in file:
            s = student.split()
            StudentList.add_item(Student(s[0],s[1],s[2],s[3],s[4]))
    except Exception:
        print("No "+FILENAME+" found")
        
def update_list()->None:
    students = StudentList.get_list()
    file = open(FILENAME, "w")
    for student in students:
        file.write(str(student)+"\n")
    file.close()

#Displays the menu title
def top_message(message:str):
    system("cls")
    print(message)
    
#Input validation module, making sure that the user filled all fields
def validation(idno:str,lastname:str,firstname:str,course:str,level:str)->bool:
    valid:bool = (idno != "" and lastname != "" and firstname != "" and course != "" and level != "")
    if not valid:
        print("Fill all fields")
    return valid

#Print student info in proper format
def print_info(student:Student)->None:
    print(f"{student.idno :<4}|\t{student.lastname:<10}|\t{student.firstname:<13}|\t{student.course:<8}|  {student.level}")
    
    
#Add student module
def addstudent():
    top_message("-------- [ADD STUDENT] --------")
    idno = input("IDNO       :")
    lastname = input("LASTNAME   :")
    firstname = input("FIRSTNAME  :")
    course = input("COURSE     :")
    level = input("LEVEL      :")
    #Input validation
    if validation(idno,lastname,firstname,course,level):
        StudentList.add_item(Student(idno,lastname,firstname,course,level))
        print("Student successfully added")
    input("Press Any Key to Continue...")
    save_list() #load the save_list module to save StudentList data to permanent file data
 
#Find student module   
def findstudent():
    top_message("-------- [ADD STUDENT] --------")
    idno = input("IDNO       :")
    status = "\nNo data found :/"
    if len(StudentList.get_list())>0:
        for student in StudentList.get_list():
            if student.__eq__(idno):
                status = "\nFound data-> "+str(student)
                break
    print(status)
    input("Press Any Key to Continue...")
    
#Delete Student module
def deletestudent():
    top_message("-------- [DELETE STUDENT] --------")
    idno = input("IDNO       :")
    status = "\nYou cannot delete data if StudentList is empty"
    if len(StudentList.get_list())>0:
        student = StudentList.search_get_object(idno)
        if student != None:
            status = "\nremoved -> "+str(StudentList.remove_item(student))
    print(status)
    input("Press Any Key to Continue...")        
        
#Update Student module     
def updatestudent():
    top_message("-------- [UPDATE STUDENT] --------")
    idno = input("IDNO       :")
    if len(StudentList.get_list())>0:
        student = StudentList.search_get_object(idno)
        if student != None:
            print("\nOLD DATA")
            print(f"IDNO\tLASTNAME\tFIRSTNAME\tCOURSE\t LEVEL")
            print_info(student)
            lastname = input("NEW LASTNAME   :")
            firstname = input("NEW FIRSTNAME  :")
            course = input("NEW COURSE     :")
            level = input("NEW LEVEL      :")
            if validation(idno,lastname,firstname,course,level):
                student = Student(idno,lastname,firstname,course,level)
                StudentList.update_item(student)
                print("Student was successfully updated")
    else: print("\nYou cannot update data if StudentList is empty")
    
    input("Press Any Key to Continue...")  
       
#Display all student module 
def displayall():
    top_message("-------- [DISPLAY ALL STUDENT] --------")
    print(f"\nIDNO\tLASTNAME\tFIRSTNAME\tCOURSE\t LEVEL")
    if len(StudentList.get_list())>0:
        for student in StudentList.get_list():
            print_info(student)
    else:
        print("...\n...\nNo data found :/")
    input("Press Any Key to Continue...")

#Everyone's favorite module
def quit():
    print("program terminated...")
    update_list()

#Get option module, returns a function
def get_option(option:int):
    menuoptions:dict={
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:updatestudent,
        5:displayall,
        0:quit,
    }
    return menuoptions.get(option)()

#Display menu module
def displaymenu()->None:
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
    
#Main module
def main():
    load_list()
    option = -1
    while option != 0:
        displaymenu()
        option=int(input("Enter Option(0..5): "))
        get_option(option)


if __name__ == "__main__": #If this file is called as a script, run the main module
    main()