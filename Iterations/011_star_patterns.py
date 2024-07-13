"""
wirte a program to Generate Inverted filled Right angle triange

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

while (rowIndex <=rowRange):
	columnIndex =1
	while(columnIndex<=rowRange-rowIndex+1):
		print("*",end=" ")
		columnIndex +=1
	print()
	rowIndex +=1