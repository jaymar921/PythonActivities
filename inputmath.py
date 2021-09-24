"""
 A program that would accept two(2) integer values
 display the sum, product, quotient, difference
"""
import os

os.system("cls")

print("A program accepts two(2) integers and display the math value")
print("Sum, Product,Quotient, Difference")

a = int(input("Enter first value(n):"))
b = int(input("Enter second value(n):"))

print("The sum of %d and %d is %d" % (a,b,(a+b)))
print("The product of %d and %d is %d" % (a,b,(a*b)))
print("The quotient of %d and %d is %.2f" % (a,b,(a/b)))
print("The difference of %d and %d is %d" % (a,b,(a-b)))