"""
wirte a program to Generate below illustration
        *
      * *
    *   *
  *     *
*       *
  *     *
    *   *
      * *
        *
"""
import os
os.system("cls")

print("\nUsing While loop\n")

rowRange = int(input("Pleae enter the rowRange:"))
rowIndex =1

starManager =1
spaceTracker =rowRange -1

while(rowIndex <=2*rowRange):
	columnIndex =1
	while (columnIndex<=spaceTracker):
		print(" ",end=" ")
		columnIndex +=1
	
	columnIndex =1
	while(columnIndex <=starManager):
		if (columnIndex == 1 or columnIndex == starManager):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		columnIndex +=1
	
	if rowIndex<rowRange:
		starManager +=1
		spaceTracker -=1
	else:
		starManager -=1
		spaceTracker +=1
	print()
	rowIndex +=1
	
print("\nUsing For loop\n")

starManager =1
spaceTracker =rowRange -1

for rowIndex in range(1,2*rowRange+1):
	for columnIndex in range(1,spaceTracker+1):
		print(" ",end=" ")
	for columnIndex in range(1,starManager+1):
		if (columnIndex == 1 or columnIndex == starManager):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	if rowIndex <rowRange :
		starManager +=1
		spaceTracker -=1
	else:
		starManager -=1
		spaceTracker +=1
	print()