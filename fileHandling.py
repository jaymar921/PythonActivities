#opening and reading a text file in python

from os import system

def main():
    system("cls")
    #get the file handle
    try:
        file = open("myFile.txt")
        print("File handle: "+str(file))
        content = file.read()
    
        print("File content: "+content)
    except Exception:
        print("File not found")

if __name__=="__main__":
    main()