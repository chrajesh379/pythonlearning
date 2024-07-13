"""
wirte a program to Generate Mirrored Hallow Right angle triange

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

while (rowIndex <=rowRange):
	columnIndex =1
	while(columnIndex<=rowRange-rowIndex):
		print(" ",end=" ")
		columnIndex +=1
	
	columnIndex =1
	while(columnIndex<=rowIndex):
		if(rowIndex == 1 or columnIndex == 1 or columnIndex == rowIndex or rowIndex == rowRange):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1
