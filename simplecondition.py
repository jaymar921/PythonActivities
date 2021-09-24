"""
    A program that would display "NEGATIVE" if the inputed
    value is less than Zero(0), "POSITIVE" if the inputed
    value is greater than Zero(0), else "ZERO"
"""
from os import system

def main():
    system("cls")
    a = int(input("Input an integer:"))
    
    if a>0:
        print("POSITIVE")
    elif a<0:
        print("NEGATIVE")
    else:
        print("ZERO")
        

if __name__ == "__main__":
    main()