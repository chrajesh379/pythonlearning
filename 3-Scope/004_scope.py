"""
Enclosing Scope
1. Enclosing Scope erises only when we are having Nested Functions
"""

def outerFunction():
	print("Outer Function Scope Begins here")
	print("Enclosing scope of the inner function")
	"1. Local Scope of the Outer Fucntion 2. Global Scope of the Program Level 3. Buit-in Scope"
	def innerFunction():
		print("Inner Function Scope Begins here")
		"1. Local Scope of the Inner Fucntion 2. Enclosing Scope of Outer Function's Local Scope 3. Global Scope of the Program Level 4. Buit-in Scope"
		return
		print("Inner Function Scope Ends here")
	return
	print("Outer Function Scope Begins here")