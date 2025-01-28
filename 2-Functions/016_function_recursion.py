"""
Head Recursion:
If we have pending work after the recrsion then Head Recursion. Its actually having some amount of pending work after the Head recursion ( Some more statements after recursion)
Tail Recusrsion:
If we haven't having pending work after the recursion then Tail Recursion
"""

"""
Head Recursion:
"""

import os
os.system("cls")

def factorial(factInput):
	if factInput==0:
		return 1
	else:
		return factInput * factorial(factInput-1)

factInput = int(input("Please Enter Factorial Number: "))
print(f"factioral of the give number {factInput} is : {factorial(factInput)}")


"""
tail recursion
"""

import os
os.system("cls")

def factorial_1(factInput,accumulator =1):
	if factInput==0:
		return accumulator
	else:
		return factorial_1(factInput-1, factInput*accumulator)

factInput = int(input("Please Enter Factorial Number: "))
print(f"factioral of the give number {factInput} is : {factorial_1(factInput,1)}")
