"""
    Using an input write
    A program that would filter a collection of string in a list
    
    Example:
    
    list=>["aplha", "bravo", "charlie","delta","echo","foxtrot","golf","hotel","india","juliet"]
    
    input: a
    
    display -> alpha, bravo, charlie, delta, india
"""
from os import system

def main():
    system("cls")
    myList = ["aplha", "bravo", "charlie","delta","echo","foxtrot","golf","hotel","india","juliet"]
    filtered_list = []
    mystr = input("Enter String: ")
    
    for item in myList:
        if mystr in item:
            filtered_list.append(item)
            
    for filtered_item in filtered_list:
        print(filtered_item, end=", ")
    filtered_list = []
    
    

if __name__ == "__main__":
    main()