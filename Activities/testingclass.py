from os import system

class myClass:
    def __init__(self, value_a, value_b):
        self.a = value_a
        self.b = value_b
        
    def printValues(self):
        print("%d + %d = %d" % (self.a, self.b,(self.a+self.b)))
        
    def getGreater(s):
        if s.a > s.b:
            print("%d is greater than %d" % (s.a,s.b))
        else:
            print("%d is greater than %d" % (s.b,s.a))
        
def main():
    system("cls")
    a = int(input("Enter first value:"))
    b = int(input("Enter second value:"))
    m = myClass(a, b)
    m.printValues()
    m.getGreater()


if __name__ == "__main__":
    main()
