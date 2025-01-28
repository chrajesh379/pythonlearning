"""
wirte a program to Generate Inverted Hollow Mirrored Right angle triange

* * * * * * * * * *
  *               *
    *             *
      *           *
        *         *
          *       *
            *     *
              *   *
                * *
                  *

"""
import os
os.system("cls")

rowRange = int(input("Pleae enter the rowRange:"))
rowIndex =1

while (rowIndex <=rowRange):
	columnIndex =1
	while(columnIndex <rowIndex):
		print(" ",end=" ")
		columnIndex +=1
	
	columnIndex =1
	while (columnIndex <=rowRange-rowIndex+1):
		if (rowIndex ==1 or columnIndex ==1 or columnIndex == (rowRange-rowIndex+1)):
			print("*",end=" ")
		else:
			print(" ",end =" ")
		columnIndex +=1
	print()
	rowIndex +=1