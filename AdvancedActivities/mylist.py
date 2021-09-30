"""
    MyList
    By Jayharron
    BSIT 3
"""
from Student import Student
class MyList(object):
    
    def __init__(self):
        self.mylist:list=[]
    
    def is_empty(self)->bool:
        """sentinel method"""
        return len(self.mylist)==0
        
    def add_item(self, item:Student)->bool:
        self.mylist.append(item)
        return True
        
    def find_item(self, item:Student)->Student:
        if self.is_empty() != True:
            for data in self.mylist:
                if data.__eq__(item):
                    return data
        raise None
       
    def search_get_index(self, item:Student)->int:
        if self.is_empty() != True:
            for data in self.mylist:
                if data.__eq__(item):
                    return self.mylist.index(data)
        raise -1
        
    def search_get_object(self, idno:str)->Student:
        if self.is_empty() != True:
            for data in self.mylist:
                if data.__eq__(idno):
                    return data
        raise None
        
    def update_item(self,item:Student)->bool:
        #Iterate, check if idno from item@param match with student from list
        for student in self.mylist:
            if student.idno == item.idno:
                if self.search_get_index(student) != -1:
                    self.mylist[self.search_get_index(item)] = item
                    return True
        raise False
        
    def remove_item(self, item:Student)->str:
        if self.search_get_index(item) != -1:
            return self.mylist.pop(self.search_get_index(item))
        raise None
    def __str__(self)->str:
        return "\n".join([str(item) for item in self.mylist])
    def get_list(self)->list:
        return self.mylist


#TESING PURPOSE
def main():
    l = MyList()
    s1 = Student("001","Abejar","Jayharron","BSIT","3")
    s2 = Student("002","Abejar","Janeharra","BSHM","2")
    l.add_item(s1)
    l.add_item(s2)
    l.add_item(Student("003","Abellana","Pia","BSIT","1"))
    print(str(l))
    print("\nFound\n"+str(l.find_item(s1)))
    print("\nRemoved\n"+str(l.remove_item(s1)))
    print("\n"+str(l))
    s2 = Student("002","Abejar","Jane","BSHM","2")
    print("\nUpdate\n"+str(l.update_item(s2)))
    print("\n"+str(l))
if __name__=="__main__":
    main()
