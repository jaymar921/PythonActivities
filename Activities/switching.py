def switchCase(arg):
    mySwitch = {
        "1": "This is option 1",
        "2": "This is option 2",
        "3": "This is option 3"
    }
    return mySwitch.get(arg,"wrong input")


def main():
    option = ""
    while option != "0":
        option = input("Enter value: ")
        
        print(switchCase(option))
        input("Press any key to continue")
        

if __name__ == "__main__":
    main()
