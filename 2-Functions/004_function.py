"""
Python will work Call by Object
If the values are not modified inside the fuction. It will be use same reference object

"""

import os
os.system("cls")

def addvalues(operand1,operand2):
	print("\nIn the function call Start and before change the values")
	print(f"\noperand 1 value is {operand1} and reference id is {id(operand1)} and hexavalue is {hex(operand1)}")
	print(f"\noperand 2 value is {operand2} and reference id is {id(operand2)} and hexavalue is {hex(operand2)}")
	print("\nIn the function call End and before change the values")
	
	print("\n\nchanging the value")
	operand1=65
	operand2=75
	
	print("\nIn the function call Start and After change the values")
	print(f"\noperand 1 value is {operand1} and reference id is {id(operand1)} and hexavalue is {hex(operand1)}")
	print(f"\noperand 2 value is {operand2} and reference id is {id(operand2)} and hexavalue is {hex(operand2)}")
	print("\nIn the function call End and After change the values")

	

op1 = int(input("Enter Operand1 value : "))
op2 = int(input("\nEnter Operand2 value : "))

print("\nbefore the function call Start")
print(f"\noperand 1 value is {op1} and reference id is {id(op1)} and hexavalue is {hex(op1)}")
print(f"\noperand 2 value is {op2} and reference id is {id(op2)} and hexavalue is {hex(op2)}")
print("\nbefore the function call End")
addvalues(op1,op2)

print("\nAfter the function call Start")
print(f"\noperand 1 value is {op1} and reference id is {id(op1)} and hexavalue is {hex(op1)}")
print(f"\noperand 2 value is {op2} and reference id is {id(op2)} and hexavalue is {hex(op2)}")
print("\nAfter the function call End")