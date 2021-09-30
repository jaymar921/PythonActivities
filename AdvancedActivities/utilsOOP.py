from random import randint
class person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getinstance(instance):
		__init__(instance.name, instance.age)

	def __str__(self):
		return f"{self.name : <15}  - \t{self.age : <2}"

	def __eq__(self, other):
		return self.name==other.name and self.age==other.age


class dataholder:
	def __init__(self):
		self.data = []
		self.count = 0

	def add(self,person):
		self.data.append(person)
		self.count+=1

	def remove(self,person):
		for p in data:
			if(p==person):
				data.remove(p)
				print("Person Removed")

	def show(self):
		print("\n\t\tDATABASE INFORMATION")
		print(f"\tID\t\t   NAME \t\tAGE")
		i = 0
		for x in self.data:
			i+=1
			print("\t"+str(i)+"\t -- \t"+str(x))


def generateperson():
	names = ["Olivia","Emma",'Ava','Charlotte','Sophia','Amelia','Isabella','Mia','Evelyn','Harper','Camila','Gianna','Abigail','Luna','Ella','Elizabeth','Sofia','Emily','Avery','Mila','Scarlett','Eleanor','Madison','Layla','Penelope','Aria','Chloe','Grace','Ellie','Nora','Hazel','Zoey','Riley','Victoria','Lily','Aurora','Violet','Nova','Hannah','Emilia','Zoe','Stella','Everly','Isla','Leah','Lillian','Addison','Willow','Lucy','Paisley','Natalie']
	return person(names[randint(0,len(names)-1)], randint(15,35))