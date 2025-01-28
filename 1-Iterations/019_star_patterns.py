"""
wirte a program to Generate below illustration
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""
import os
os.system("cls")

print("\nUsing While loop\n")

rowRange = int(input("Pleae enter the rowRange:"))
rowIndex =1
columnTracker =1
while (rowIndex <= 2*rowRange):
	columnIndex =1
	while (columnIndex <=columnTracker):
		print("*",end=" ")
		columnIndex +=1
	if rowIndex <rowRange :
		columnTracker +=1
	else:
		columnTracker -=1
	print()
	rowIndex +=1
	
print("\nUsing For loop\n")

columnTracker =1
for rowIndex in range(1,2*rowRange+1):
	for columnIndex in range(1,columnTracker+1):
		print("*",end=" ")
	if rowIndex <rowRange :
		columnTracker +=1
	else:
		columnTracker -=1
	print()