"""
Variable argument functions

* args . here * is called unpacking operator. It will take the number of parameters at the time of run time 
** kwargs

"""


import os
os.system("cls")

def addvalues(*args):
	calsum =0
	for index in args:
		calsum += index
	return calsum

executechoice = int(input("Enter number of the arguments : "))
if executechoice ==1: 
	op1 = int(input("\nEnter number first argument : "))
	result = addvalues(op1)
	print(f"\n result is {result}")
elif executechoice ==2:
	op1 = int(input("\nEnter number first argument : "))
	op2 = int(input("\nEnter number second argument : "))
	result = addvalues(op1,op2)
	print(f"\n result is {result}")
elif executechoice ==3:
	op1 = int(input("\nEnter number first argument : "))
	op2 = int(input("\nEnter number second argument : "))
	op3 = int(input("\nEnter number second argument : "))
	result = addvalues(op1,op2,op3)
	print(f"\nresult is {result}")
elif executechoice ==4:
	op1 = int(input("\nEnter number first argument : "))
	op2 = int(input("\nEnter number second argument : "))
	op3 = int(input("\nEnter number third argument : "))
	op4 = int(input("\nEnter number Fourth argument : "))
	result = addvalues(op1,op2,op3,op4)
	print(f"\nresult is {result}")