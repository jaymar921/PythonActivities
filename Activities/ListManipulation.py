"""
	List manipulation
    -----------------
    Python Collection(Built-in Data Structures)
    ------------------------------------------
    1. List - portrays the built-in array of Python
            - an ordered(elements have ordinal relationship with other elements in the container)
             & indexed
            - allows duplicate data
            - mutable(add, update, delete, retrieve)
           example:   myList = []
           
    2. Tuple - non-mutable(cannot update,delete,add during runtime) list
        example: myTuple = (1,2,3,4)
        
    3. Set - un-ordered and un-indexed collection of distinct(no duplicate),
           - mutable
         example: mySet = {"a","b","c"}
         
    4. Dictionary - structured collection of data elements, also mutable
                  - no duplicates
                  - uses key value pairs
         example: myDictionary = {
                        1:add,
                        2:find,
                        3:delete,
                        4:display,
                        0:quit
                    }
"""
from os import system

def main():
    system("cls")
    myString = [] #Empty List
    #adding new list items
    myString.append(10)
    myString.append(25)
    myString.append(42)
    myString.append(12)
    
    #Populate the list by list instantiation
    myString=list((10,25,42,12))
    print(myString)
    #removing items from the list
    #using the pop() module
    #pop - returns the removed value
    item = myString.pop()
    print(myString)
    print(item)
    #using remove() module
    #remove - delete the selected item from the list
    #but does not return the item
    myString.remove(10)
    print(myString)
    #updating the element in the list
    myString[0] = 120
    print(myString)
    #New List
    myList=[88,20,34,5,10,7,23,100]
    #sort(arrange)
    myList.sort() #ascending
    print(myList)
    myList.sort(reverse=True) #descending
    print(myList)
    #Inserting new item in the list
    myList.insert(1, "jay")
    print(myList)
    #Displaying the list programmatically
    for x in myList:
        print(x)
    #using short cut
    print("using short cut")
    [print(x, end=", ") for x in myList]
    #Converting list to string
    #using join() module
    print()
    newstring = ",".join([str(x) for x in myList])
    print(newstring)
    #Convert String to List
    myStr = "The Quick brown fox jumps over the lazy dog"
    
    mystrList=myStr.split()
    print(mystrList)



if __name__=="__main__":
    main()
