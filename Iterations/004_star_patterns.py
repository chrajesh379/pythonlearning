"""
wirte a program to Generate Square or Rectangle Hollow Rhombus Parrern

         * * * * * * * * * *
        *                 *
       *                 *
      *                 *
     *                 *
    *                 *
   *                 *
  *                 *
 *                 *
* * * * * * * * * *

"""
import os
os.system("cls")

rowRange = int(input("Please enter rowRange:"))
rowIndex =1

while (rowIndex <=rowRange):
	columnIndex =1
	while (columnIndex<=rowRange-rowIndex):
		print(" ",end=" ")
		columnIndex +=1
	
	columnIndex =1
	while (columnIndex<=rowRange):
		if (rowIndex ==1 or rowIndex==rowRange or columnIndex ==1 or columnIndex ==rowRange):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1
		