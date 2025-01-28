"""
wirte a program to Generate Hollow Right angle triange

*
**
* *
*  *
*   *
*    *
*     *
********

"""
import os
os.system("cls")

rowRange = int(input("Please enter the rowRange:"))
rowIndex =1
while (rowIndex <=rowRange):
	columnIndex =1
	while (columnIndex <=rowIndex):
		if (rowIndex == 1 or rowIndex == rowRange or columnIndex == 1 or columnIndex == rowIndex):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		columnIndex +=1
		
	print()
	rowIndex +=1
	