"""
wirte a program to Generate Hollow Square or Rectangle Parrern with diagonals filled

***********
**       **
* *     * *
*  *   *  *
*   * *   *
*    *    *
*   * *   *
*  *   *  *
* *     * *
**       **
***********

"""
import os
os.system("cls")

rowRange = int(input("Please enter the rowRange:"))
if rowRange%2==0:
	rowRange +=1

rowIndex =1 

while (rowIndex<=rowRange):
	columnIndex =1
	while (columnIndex<=rowRange):
		if (rowIndex ==1 or rowIndex==rowRange or columnIndex == 1 or columnIndex == rowRange or  columnIndex==rowIndex or columnIndex == (rowRange-rowIndex+1)):
			print("*",end ="")
		else:
			print(" ",end="")
		columnIndex +=1
	print()
	rowIndex +=1