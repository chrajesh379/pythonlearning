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
	
	for index in range(10):
		print(f"Sequence of numbers from {parm01} is {innerFunctionAddress(index)}")