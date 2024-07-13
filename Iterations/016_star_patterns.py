"""
wirte a program to Generate Hollow Pascals triange

          *
         * *
        *   *
       *     *
      *       *
     *         *
    *           *
   *             *
  *               *
 * * * * * * * * * *
"""
import os
os.system("cls")

rowRange = int(input("Pleae enter the rowRange:"))
rowIndex =1

print("\nUsing While loop")
while (rowIndex <=rowRange):
	columnIndex =1
	while(columnIndex <=rowRange-rowIndex+1):
		print("",end=" ")
		columnIndex +=1
	
	columnIndex =1
	while (columnIndex <=rowIndex):
		if (rowIndex == 1 or columnIndex == 1 or rowIndex == rowRange or columnIndex == rowIndex ):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1

print("\nUsing For loop")

for rowIndex in range(1,rowRange+1):
	for columnIndex in range(rowRange-rowIndex+1):
		print("",end=" ")
	for columnIndex in range(1,rowIndex+1):
		if (rowIndex == 1 or columnIndex == 1 or rowIndex == rowRange or columnIndex == rowIndex ):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
