"""
wirte a program to Generate Right angle triange

*
**
***
****
*****
******
*******

"""
import os
os.system("cls")

rowRange = int(input("Please enter rowRange:"))
rowIndex =1

while (rowIndex<=rowRange):
	columnIndex =1
	while columnIndex<=rowIndex:
		print("*",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1
