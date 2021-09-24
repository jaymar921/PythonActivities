"""
    Manipulating Python String
"""
from os import system

myString = "Welcome to University of Cebu"

multiLineString = """
    University of Cebu
    Main campus
    
    College of Computer Studies
    Sanciangko St., Cebu City
"""

string1 = "University "
string2 = "of "
string3 = "Cebu"
myString1 = string1+string2+string3

def main():
    system("cls")
    i = 0
    for c in myString:
        print("[%d]=%c" % (i,c))
        i+=1
    print(myString[:2]) # Print everything before the index 2
    print(myString[2:]) # Print everything starts with index 2
    print(myString[5:10]) # Print everything starts with index 5 and before index 10
    print(myString[5:2]) # No error, but no output
    
    print(myString.upper()) #Display the string in capitalize format
    print(myString.lower()) #Display the string in lower format
    print(myString.startswith("University"))
    print(myString.startswith("Welcome"))
    print(myString.isupper())
    
    mylist = list(myString)
    print(mylist)
    
    myTuple = tuple(myString) #Tuple is immutable list
    print(myTuple)
    
    for x in mylist:
        print(x)
        
    #Convert number into String
    value = 1000
    myValue = "P"+str(value)
    print(myValue)
    #Display the length of the string
    print("the string length: %d" % len(myString))
    
    print("Is 'v' in myString? ", "v" in myString)
    print("Is 'a' in myString? ", "a" in myString)
    
    
    
if __name__ == "__main__":
    main()