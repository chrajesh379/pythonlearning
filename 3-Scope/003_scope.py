"""

"""

import os
os.system("cls")

# Global Scope of the program Begins here 
myGlobalvalue = 45

def outerFunction():
	# Local Scope of the outerFunction Begins here
	print("\nouterFunction Started")
	print(f"Global Scope of the variable myGlobalvalue is : {myGlobalvalue}")
	myOuterValue = 50
	print(f"Local Scope of the outerFunction variable myOuterValue is : {myOuterValue}")
	
	def innnerFunction():
		# Local Scope of the innnerFunction Begins here
		print("\ninnnerFunction Started")
		myInnervalue = 60
		print(f"Global Scope of the variable myGlobalvalue is : {myGlobalvalue}")
		print(f"Enclosing Scope of the outerFunction variable myOuterValue is : {myOuterValue}")
		print(f"Local Scope of the innnerFunction variable myInnervalue is : {myInnervalue}")
		print("\n innnerFunction Ended")
		return
		# Local Scope of the innnerFunction Ends here
	innnerFunction()
	print("\n outerFunction Ended")
	return 
	# Local Scope of the outerFunction Ends here
print(f"Global Scope of the variable myGlobalvalue is  {myGlobalvalue}")
outerFunction()
#innnerFunction() # We can't call innnerFunction() because it is in the outerFunction() local scope
#print(f"Local Scope of the outerFunction variable myOuterValue is  {myOuterValue}") # This will give an error . because it is out of scope
#print(f"Local Scope of the innnerFunction variable myInnervalue is : {myInnervalue}") # This will give an error . because it is out of scope
# Global Scope of the program Ends here 