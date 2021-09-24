"""
    NAME: ABEJAR, JAYHARRON MAR C
    EDP CODE: 04549
    SUBJECT: ITELECT-PYTHON
    CLASS SCHEDULE: 9:00-11:30AM TTH
    
    ASSIGNMENT: Convert this menu program using the switch statement

    A program that would accept two integer values
    create a simple menu for the user to get the simple
    math operation of his/her option.
    
    ----MENU----
    1.add
    2.multiply
    3.subtract
    4.divide
    0.quit
    ------------
    Enter Option(0..4):
    
"""
import os

menuitem = (
    "----MENU----",
    "1.add",
    "2.multiply",
    "3.subtract",
    "4.divide",
    "0.quit",
    "------------"
)

def displaymenu():
    os.system("cls")
    for menu in menuitem:
        print(menu.upper())

def usingSwitch(arg):
    if arg == "0":
        return "Program Terminated..."
    
    a = int(input("Enter first value:"))
    b = int(input("Enter first value:"))
    switcher = {
        "1": "The sum of %d and %d is %d" % (a,b,(a+b)),
        "2": "The product of %d and %d is %d" % (a,b,(a*b)),
        "3": "The difference of %d and %d is %d" % (a,b,(a-b)),
        "4": "The divide of %d and %d is %.2f" % (a,b,(a/b)),
    }
    return switcher.get(arg, "invalid argument")

def main():
    option = ""
    while option != "0":
        displaymenu()
        option = input("Enter Option(0..4):")
        
        print(usingSwitch(option))
        input("Press Any key to continue...")
    

if __name__ == "__main__":
    main()