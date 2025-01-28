"""
GCD 

ex: 
num1 = 88
num2 = 24

1 : gcd(88,24)
2 : gcd(24,16)    88%24 is 16
3 : gcd(16,8)     24%16 is 8
4 : gcd(8,0)      16%8 is 0
5 : return 8
"""

import os
os.system("cls")

def gcd(num1,num2):
	if num2==0:
		return num1
	else:
		return gcd(num2,num1%num2)

num1 = int (input("Please enter number 1 : "))
num2 = int (input("Please enter number 2 : "))
print(f"gcd for the given number {num1} and {num2} is : {gcd(num1,num2)}")