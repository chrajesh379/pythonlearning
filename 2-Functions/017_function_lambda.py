"""
Anonymous functions in general called as lambda functions
Entire logic will be designed in one line. Limited for single expression.

Basic Syntax:

lambda functionArguments:Lambda Expression
"""

import os 
os.system("cls")

def convertupper(s):
	return s.upper()

name = input("Please enter the name: ")
print(f"Given Name is : {name} and converting to upper is : {convertupper(name)}")
out = lambda s:s.upper()
print("\nUsing Lambda Funcitons")
print(f"\nGiven Name is : {name} and converting to upper is : {out(name)}")
print("\nUsing Lambda Funcitons having print statement")
getvalue = lambda name: print(f"\nGiven Name is : {name} and converting to upper is : {out(name)}")
getvalue(name)

x = int(input("\nEnter first number :"))
y = int(input("\nEnter second number :"))

add = lambda x,y : x+y
print(f"\naddition of numbers are {add(x,y)}")