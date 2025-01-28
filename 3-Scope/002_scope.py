"""
enclosing scope : Enclosing scope will come only when we are having Nested functions

"""

def OuterFunciton():
	#local scope of the OuterFunction is begins Here
	# This scope in outer Function is enclosing scope to innnerFunction(). Anything declared here , can be used in innnerFunction()
	# Total Three scopes are available 1. Local Scope of OuterFunciton() (First Priority) 2. Global Scope of Program Level (Second Priority) 3. Built in Scope of Program Language Level
	
	
	def innnerFunction():
		#local scope of the innnerFunction is begins Here
		# Total Four scopes are available 1. Local Scope of innnerFunction() (First Priority) 2.Enclosing Scope of the OuterFunction Local Scope 3. Global Scope (Third Priority)
		# 4. Built in Scope of Program Language Level
		
	
		return
		#local scope of the innnerFunction is Ends Here
	
	return
	#local scope of the OuterFunction is Ends Here