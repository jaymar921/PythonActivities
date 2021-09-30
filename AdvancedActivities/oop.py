from os import system
import utilsOOP as util

database = util.dataholder()

def main():
	system("cls")
	person = util.person("Jay Abejar", 21)
	person1 = util.person("Pia Abellana", 19)
	database.add(person)
	database.add(person1)
	for x in range(0,20):
		database.add(util.generateperson())
	
	database.show()


if __name__ == "__main__":
	main()