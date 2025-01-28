"""
Use of Args and Kwargs
"""

def adder(*args):
	x=0
	for i in args:
		x=x+i
	print(f"sum is : {x}")

def intro(**data):
	for key ,value in data.items():
		print(f"Key is {key} and value is {value}",end="\n")
		
adder(1,2,3,4)
print("")
adder(1,2,3,5,6)
print("")
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
print("")
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)