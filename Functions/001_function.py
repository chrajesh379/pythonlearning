"""
Four design approaches:
1. Function Not accepting Parameters and not returning any value
2. Function accepting Parameters and not returning any value
3. Function Not accepting Parameters and returning any value
4. Function accepting Parameters and returning any value

"""

import os
os.system("cls")

def add(op1,op2):
# op1 and op2 are called Formal parameters
	return (op1+op2)
	
def factorial(n):
	if n<=1:
		return 1
	return n * factorial(n-1)

op1 = int(input("please enter first value: "))
op2 = int(input("\nplease enter second value: "))

# op1 and op2 are called actual parameters
result = add(op1,op2)
print(f"\nresult is {result}")
fact_input = int(input("\nplease enter factorial value: "))
f = factorial(fact_input)
print(f"\factorial is {f}")
