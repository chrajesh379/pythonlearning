"""
wirte a program to Generate below illustration
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
import os
os.system("cls")

print("\nUsing While loop\n")

rowRange = int(input("Pleae enter the rowRange:"))
rowIndex =1

spaceManager =rowRange-1
starManager = 1
while(rowIndex <=2*rowRange):
	columnIndex =1
	while (columnIndex <=spaceManager):
		print(" ",end=" ")
		columnIndex +=1
		
	columnIndex =1
	while(columnIndex<starManager*2):
		if ( columnIndex ==1 or columnIndex == starManager*2 -1 ):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		columnIndex +=1
	
	if rowIndex <rowRange:
		starManager +=1
		spaceManager -=1
	else:
		starManager -=1
		spaceManager +=1
	print()
	rowIndex +=1