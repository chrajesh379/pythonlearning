"""

"""
import os
os.system("cls")

def stringmaker(*args):
	return ' '.join(args)
	
def printarguments(*args):
	print("arguments \n")
	for argumentId , name in enumerate(args,start=1):
		print(f"{argumentId} : {name}")
		
def printinformation(name,age,*args):
	print(f"\nname of the person : {name} and age is : {age}\n")
	for argumentid,argname in enumerate(args,start=1):
		print(f"{argumentid} . {argname}")
	
print(f"\nString maker of 'Rajesh','Chittineni' is:  {stringmaker('Rajesh','Chittineni')}")
print(f"\nString maker of 'Sathish','Kumar','Yellanki' is:  {stringmaker('Sathish','Kumar','Yellanki')}")

printarguments("Cricket","Hockey","FootBall",'Chess','Batminton')
printinformation("Rajesh",37,"Likes Cricket","Play Tennies","Play Chess")
printinformation("Raj",32,"Like Book Reading","Likes Playing","Likes Driving","Likes Coding")
