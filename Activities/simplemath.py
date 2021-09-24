"""
	A program that would display the sum, product, quotient
	difference of th two integer values 10 and 20
"""
#Import OS
from os import system

system("cls")

a,b = 10, 20
#a = 10
#b = 20
#a, b = b, a <- swap

# ctrl + d, repeat the line
print("Sum of %d and %d is %d" % (a,b, (a+b)))
print("Product of %d and %d is %d" % (a,b, (a*b)))
print("Quotient of %d and %d is %.2f" % (a,b, (a/b)))
print("Difference of %d and %d is %d" % (a,b, (a-b)))
