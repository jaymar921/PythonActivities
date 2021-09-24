from os import system

def main():
    dictionary = {
        1:"hello",
        2:"world",
        3:"bruh"
    }
    [print(dictionary[x]) for x in dictionary]

if __name__ == '__main__':
	main()