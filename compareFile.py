'''
    Abejar, Jayharron Mar
    04549 IT-ELPYTHON
    9:00-11:30 TTH
    
    Activity 3
    Read two(2) files, compare all contents in a file, and compute
    the percentage(%) similarity of two(2) files.
    
    Allow the user to type the name of files to compare
    
    Use set, List and other implements for this application
'''
from os import system

def main():
    system("cls")
    askInput()
    print("Program Terminated")
    
def askInput():
    print("Compare two(2) files")
    file1 = input("Enter first filename: ")
    file2 = input("Enter second filename: ")
    content1 = ""
    content2 = ""
    
    try:
        content1 = open(file1).read().split()
    except Exception:
        print("Could not find "+file1+" - program exit")
        return
    try:
        content2= open(file2).read().split()
    except Exception:
        print("Could not find "+file1+" - program exit")
        return
    compare(content1, content2)

def compare(a, b):
    setA = set(a)
    setB = set(b)
    intersect = 0
    total = 0
    if len(setA) > len(setB):
        intersect = len(setA.intersection(setB))
        total = len(setA)
    else:
        intersect = len(setB.intersection(setA))
        total = len(setB)
    
    percent = intersect/total
    print("Content Similarity: %.2f Percent" % (percent*100))
    
    
    
    
    

if __name__=="__main__":
    main()