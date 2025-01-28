"""
scoping
"""
import os
os.system("cls")

myGlobalvar = 35 
print(f"")

def outerFunction():
	myOuterVar = 55
	print(f"Local Scope of the outer Function Started")
	print(f"Local scope of the Outer Function variable usage myOuterVar in outerFunction is : {myOuterVar}")
	print(f"Global scope of the Program Level variable usage myGlobalvar in outerFunction is  : {myGlobalvar}")
	def innerFunction():
		myInnerVar = 25
		print(f"Local Scope of the Inner Function Started")
		print(f"Local scope of the Inner Function variable usage myInnerVar in innerFunction is : {myInnerVar}")
		print(f"Enclosing scope of the Outer Function variable usage myOuterVar in innerFunction is : {myOuterVar}")
		print(f"Global scope of the Program Level variable usage myGlobalvar in innerFunction is : {myGlobalvar}")
		return
	
	innerFunction()
	return
print(f"Global Scope of the Program Level Started")
print(f"Global scope of the Program Level variable usage myGlobalvar is : {myGlobalvar}")
outerFunction()

