"""
wirte a program to Generate reverse Pascals triange

* * * * * * * * * *
 * * * * * * * * *
  * * * * * * * *
   * * * * * * *
    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
"""
import os
os.system("cls")

rowRange = int(input("Pleae enter the rowRange:"))
rowIndex =1

print("\nUsing While loop\n")

while (rowIndex <=rowRange):
	columnIndex =1
	while (columnIndex <rowIndex):
		print(" ",end="")
		columnIndex +=1
	
	columnIndex =1
	while (columnIndex<=rowRange-rowIndex+1):
		print("*",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1
	
print("\nUsing For loop\n")

for rowIndex in range(1,rowRange+1):
	for columnIndex in range(rowIndex+1):
		print(" ",end="")
	for columnIndex in range(1,rowRange-rowIndex+1+1):
		print("*",end=" ")
	print()