"""
Closure:
1. It is combination of a function Bundled Together with All its references to its surrounding states.
Function will start return the address of the inner function and operate independantly 
2. Closures are possible when 
	1. We have nested functions
	2. Nested Function referes to a variable of the Outer Function
	3. The enclosing function returns the encloused Function

Disadvantgaes :
	Memory 

"""

import os
os.system("cls")

def outerFunction():
	outerMessage = "This is Enclosed scope"
	def innerFunction():
		print(f"Data from enclosed scope is called from Inner Function is {outerMessage}")
		return
	
	print(f"Inner Function Addreess is {innerFunction}")
	return innerFunction
	
if __name__=="__main__":

	innerfucntionAddress = outerFunction()
	print(f"Inner Function Address after calling Outer Function is {innerfucntionAddress}")
	innerfucntionAddress()
	