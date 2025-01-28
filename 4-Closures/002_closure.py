"""
"""

import os
os.system("cls")

def outerFunction(parm01):
	def innerFunction(parm02):
		return parm01+parm02
	return innerFunction

if __name__ == "__main__":
	parm01 = int(input("Please Enter first Value: "))
	innerFunctionAddress= outerFunction(parm01)
	parm02 = int(input("Please Enter Second Value: "))
	print(f"Sum of {parm01} and {parm02} is {innerFunctionAddress(parm02)}")