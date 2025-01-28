"""
addition and substraction

"""

import os
os.system("cls")

add = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y
rem = lambda x,y : x%y

num1 = int(input("Please enter number 1 : "))
num2 = int(input("\nPlease enter number 2 : "))
print("Enter you choice\n")
print("\n1.Addition")
print("\n2.Substraction")
print("\n3.Multiplication")
print("\n4.Division")
print("\n5.Remainder")
choice = input("\nPlease enter choice : ")

if choice=='1':
	print(f"The Sum of {num1:0.2f} and {num2:0.2f} is : {add(num1,num2)}")
elif choice=='2':
	print(f"The Substraction of {num1:.2f} and {num2:.2f} is : {sub(num1,num2)}")
elif choice=='3':
	print(f"The Multiplication of {num1:.2f} and {num2:.2f} is : {mul(num1,num2)}")
elif choice=='4':
	print(f"The Division of {num1:.2f} and {num2:.2f} is : {div(num1,num2)}")
elif choice=='5':
	print(f"The Remainder of {num1:.2f} and {num2:.2f} is : {rem(num1,num2)}")