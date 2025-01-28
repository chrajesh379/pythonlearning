"""
wirte a program to Generate Square or Rectangle Mirrored Rhombus Parrern or Horizontal Flip

* * * * * * *
  * * * * * * *
    * * * * * * *
      * * * * * * *
        * * * * * * *
          * * * * * * *
            * * * * * * *

"""
import os
os.system("cls")

rowRange = int(input("Please enter rowRange:"))
rowIndex =1

while (rowIndex <=rowRange):
	columnIndex =1
	while (columnIndex<rowIndex):
		print(" ",end=" ")
		columnIndex +=1
	
	columnIndex =1
	while (columnIndex<=rowRange):
		print("*",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1