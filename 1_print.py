import os

#Clear the screen
os.system("cls")

#default end is new line 
print("\n Outout of python first program Line 1 ", end ="")
#appended to the above line
print("Outout of python first program Line2", end ="")
print("\n Outout of python first program Line3", end ="\n")
print("addiotional space will be added if comma is there between strinf")
print("This is default space between strings","string1","string2","string3")
print("if we need to change the seperator and it can be multiple characters")
print("This is default space between strings","string1","string2","string3",sep=":")
print("This is default space between strings","string1","string2","string3",sep="*-*")
print("writing into a file")
with open(r"C:\Rajesh\OneDrive\Rajesh\Github_Code\pythonlearning\printoutput.txt",mode="w") as f:
  print("Outout of python first program",file=f)