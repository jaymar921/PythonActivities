# set - un-ordered, un-indexed linear collection of distinct(unique) data elements
from os import system

def main():
    system("cls")
    #myset={} <- dictionary if empty
    #myset = set()
    myset = {'a','b','c','d'} # <- set if not empty
    print(type(myset))
    print(myset)
    
    mysetA = {1,2,3,4,5}
    #Create another variable reference
    #to the set pointed by mysetA
    mysetB = mysetA
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    mysetB.add(6)
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    mysetA.remove(3)
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB)+"\n")
    
    mysetC = {1,2,3,4,5}
    #Copy the contents of mySetC
    mysetD = mysetC.copy()
    print("SET C"+str(mysetC))
    print("SET D"+str(mysetD))
    mysetD.add(6)
    print("SET C"+str(mysetC))
    print("SET D"+str(mysetD))
    mysetC.remove(3)
    print("SET C"+str(mysetC))
    print("SET D"+str(mysetD))
    
    #using set operations
    mysetA={1,2,3,4,5}
    mysetB={4,5,6,7,8,9}
    
    mysetC=mysetA.union(mysetB)
    print("Union")
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    mysetC=mysetA.intersection(mysetB)
    print("Intersection")
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    mysetC=mysetA.symmetric_difference(mysetB)
    
    # update 
    # mysetA.update(mysetB)
    
    print("Symmetric Difference")
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    mysetC=mysetA.difference(mysetB)
    print("Difference A-B")
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    mysetC=mysetB.difference(mysetA)
    print("Difference B-A")
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    
    print("is set A a subset of set B")
    mysetC = mysetA.union(mysetB)
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    print(mysetA.issubset(mysetC))
    
    print("is set C a super set of set B")
    mysetC = mysetA.union(mysetB)
    print("SET A"+str(mysetA))
    print("SET B"+str(mysetB))
    print("SET c"+str(mysetC))
    print(mysetC.issuperset(mysetB))

if __name__=="__main__":
    main()
