"""
wirte a program to Generate Hollow Square or Rectangle Parrern

********
*      *
*      *
*      *
********

"""
import os
os.system("cls")

rowRange = int(input("please enter the rowRange:"))
columnRange = int(input("please enter the columnRange:"))
rowIndex =1

while (rowIndex<=rowRange):
	columnIndex =1
	while (columnIndex<=columnRange):
		if (rowIndex==1 or rowIndex==rowRange or columnIndex==1 or columnIndex==columnRange):
			print("*",end="")
		else:
			print(" ",end="")
		columnIndex +=1
	print()
	rowIndex +=1