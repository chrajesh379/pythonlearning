"""
What is Scoping in Python

1. Any identifier declared in the python Application can only be accessed in the area which is defined 
2. Once the scope of the object is Lost then the identifier is no more available in the operational memoery of the application
3. Within the same scope we canot have same names
4. In Python Scope is Managed by Rule called "LEGB"
    L: Local,Function Scope
	E: Enclosed , Non-Local Scope
	G: Global, Module Scope
	B: Built-in, Programming Language Level Scope
	
Order of the Search is L=>E=>G=>B

"""

#!python3
#The Global Scope of the python program Begins Here

import os                            #scope of the importing os module is Global
os.system("cls")                     #scope of the os.system module is Global. We are calling system function global , but it is calling Built in scope to get OS module

def raiseValue(inBaseValue):
	#local scope of the function raiseValue Begins here
	print(inBaseValue)

	return
	#local scope of the function raiseValue Ends here

raiseValue(4)
# we can't access the local scope of the function raiseValue
#The Global Scope of the python program Ends Here