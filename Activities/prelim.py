#prelim

My_list = [1,3,5,7,9,11]

My_list_2 = range(1,13,2)

[print(x) for x in My_list_2]

[print(x,end=",") for x in range(10,60)] 

d = {
    "a":"jay",
    "b":"pia"
}
print(d.get("b"))


from math import sqrt
print(sqrt(2))
b = 3.1415926
print("The value of the PI = %.4f" % b)

Colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

print(Colors[2])

mydict={ 1:'alpha',2:'bravo',3:'charlie',4:'echo'}

[print(str(x+1)+"-"+mydict.get(y),end=" | ") for x,y in enumerate(mydict)]

a,b,c=10,20,30

print(a,b,c)
 
s=[10,50,90,40,20,30]
a=s.pop(3)
print(a)

aa = {"hobbies":["reading","running"]}

for x in aa:
    print(x)
    
print(type(aa))
    
print("greater"[2:5])
