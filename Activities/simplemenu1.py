"""
    Creating a console menu in python.
    Simple Math Application
    
    ---- Menu ----
    1.ADD
    2.SUBTRACT
    3.MULTIPLY
    4.DIVIDE
    0.QUIT/END
    --------------
    Enter Option(0..4):
"""
from os import system
from myoperations import add, subtract, multiply, divide, error, accept, quit

def displayMenu():
    menu = (
        "---- Menu ----",
        "1.ADD",
        "2.SUBTRACT",
        "3.MULTIPLY",
        "4.DIVIDE",
        "0.QUIT/END",
        "--------------"
    )
    for menuItem in menu:
        print(menuItem)
        
def switch(i):
    mymenu = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        0: quit,
    }
    mymenu.get(i, error)()

def main():
    option = -1
    while option != 0:
        system("cls")
        print("Simple Math Application")
        displayMenu()
        option = int(input("Enter Option (0..4):"))
        switch(option)
        input("Press Any key to continue")

if __name__ == "__main__":
    main()
