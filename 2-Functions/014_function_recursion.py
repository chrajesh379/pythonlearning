"""
Write a program to check the given string is palindrome or not
If we reverse the string and get the same string then it is palindrome
"""

import os
os.system("cls")

def ispalidrome(strinput):
	if len(strinput)<=1:
		return True
	else:
		return strinput[0]==strinput[-1] and ispalidrome(strinput[1:-1])

strinput = input("please enter the input string: ")
print(ispalidrome(strinput))