"""
Factorial of given number
Explanation:

factorial(5) = 5*factorial(4)
factorial(4) = 4*factorial(3)
factorial(3) = 3*factorial(2)
factorial(2) = 2*factorial(1)
factorial(1) = 1*factorial(0)
factorial(0) = 1

5 * (4*factorial(3)) 
5 * 4 * (3*factorial(2)) 
5 * 4 * 3 * (2*factorial(1)) 
5 * 4 * 3 * 2 *(1*factorial(0)) 
5 * 4 * 3 * 2 *1 *1

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


