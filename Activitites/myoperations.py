def accept():
    a = int(input("Enter First Value:"))
    b = int(input("Enter Second Value:"))
    return a, b

def add():
    print("Addtion Operation")
    x,y = accept();
    print("The sum of %d and %d is %d" % (x,y,(x+y)))
def subtract():
    print("Subtraction Operation")
    x,y = accept();
    print("The difference of %d and %d is %d" % (x,y,(x-y)))
def multiply():
    print("Multiplication Operation")
    x,y = accept();
    print("The product of %d and %d is %d" % (x,y,(x*y)))
def divide():
    print("Division Operation")
    x,y = accept();
    print("The quotient of %d and %d is %.2f" % (x,y,(x/y)))
def quit():
    print("Program Exit")
def error():
    print("Accept only 0..4")
