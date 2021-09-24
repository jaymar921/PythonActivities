"""
    String filter on String list
"""
from os import system

names = ["hotel","kilo","alpha","zulu","oscar",
        "bravo","delta","charlie","india","november",
        "tango","victor","whiskey","foxtrot","golf",
        "echo","mike","xray","quebec"]

def main():
    system("cls")
    print(names)
    filter = input("Search name:")
    filterednames = [item for item in names if filter in item]
    print(filterednames)

if __name__=="__main__":
    main()