import os
os.system("cls")

print("pattrens program", end="\n")
print("1.number pattren program")
print("Outer Loop will dicate Rows and Inner loop will dicate columns")
print("""
number program : 1
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

number program : 2

*
* *
* * *
* * * *
* * * * *

number program : 3

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

number program : 4

* * * * *
* * * *
* * *
* *
*

number program : 5

number program : 13

*                   *
* *               * *
* * *           * * *
* * * *       * * * *
* * * * *   * * * * *
* * * * *   * * * * *
* * * *       * * * *
* * *           * * *
* *               * *
*                   *

number program : 14

0  
0  1  
0  2  4  
0  3  6   9  
0  4  8   12  16  
0  5  10  15  20  25  
0  6  12  18  24  30  36

number program : 15

* * * * *
*       *
*       *
*       *
* * * * *

number program : 16

* * * * * * * * * *
* *             * *
*   *         *   *
*     *     *     *
*       * *       *
*       * *       *
*     *     *     *
*   *         *   *
* *             * *
* * * * * * * * * *

""")
numprogram = int(input("chose number program:"))

if (numprogram==1):
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{columnindex}" , end=" ")
			columnindex += 1
		print("")
		rowindex +=1
elif numprogram==2:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"*" , end=" ")
			columnindex += 1
		print("")
		rowindex +=1
elif numprogram==3:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=RowLoop-rowindex+1:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{columnindex}" , end=" ")
			columnindex += 1
		print("")
		rowindex +=1
elif numprogram==4:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=RowLoop-rowindex+1:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"*" , end=" ")
			columnindex += 1
		print("")
		rowindex +=1
elif numprogram==5:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{rowindex}" , end=" ")
			columnindex += 1
		print("")
		rowindex +=1
elif numprogram==6:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = rowindex
		while columnindex>=1:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{columnindex}" , end=" ")
			columnindex -= 1
		print("")
		rowindex +=1
elif numprogram==7:
	RowLoop = int(input("Please enter row number:"))

	rowindex = RowLoop
	while rowindex>=1:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = rowindex
		while columnindex>=1:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{columnindex}" , end=" ")
			columnindex -= 1
		print("")
		rowindex -=1
elif numprogram==8:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	start = 1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{start}" , end=" ")
			columnindex += 1 
			start +=1
		print("")
		rowindex +=1
elif numprogram==9:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
	start = 1
	curr_num =1
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"{curr_num}" , end=" ")
			columnindex += 1 
			curr_num = curr_num-1
		print("")
		rowindex +=1
		start +=rowindex
		curr_num = start
elif numprogram==10:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1

	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = RowLoop
		num =1
		while columnindex>=1:
			#print(f"innerloop iteration level is: {columnindex}")
			if (columnindex>rowindex):
				print(" ",end=" ")
			else:
				print(f"{num}" , end=" ")
				num +=1
			columnindex -= 1 
		print("")
elif numprogram==11:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1

	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = RowLoop
		while columnindex>=1:
			#print(f"innerloop iteration level is: {columnindex}")
			if (columnindex>rowindex):
				print(" ",end=" ")
			else:
				print(f"*" , end=" ")
			columnindex -= 1 
		print("")
		rowindex +=1

elif numprogram==12:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1

	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"*" , end=" ")
			columnindex += 1 
		print("")
		rowindex +=1
	print("")
	
	rowindex = RowLoop
	
	while rowindex>=1:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"*" , end=" ")
			columnindex += 1 
		print("")
		rowindex -=1
		
elif numprogram==13:
	RowLoop = int(input("Please enter row number:"))

	rowindex = 1
    #first section
	while rowindex<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex = 1
		while columnindex<=rowindex:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"*" , end=" ")
			columnindex += 1 
		
		columnindex = 1
		while columnindex<=(RowLoop-rowindex+1):
			print(f" ",end=" ")
			columnindex += 1
		
		columnindex = 1
		while columnindex<=RowLoop:
			if columnindex>=RowLoop-rowindex+1:
				print(f"*",end=" ")
			else:
				print(f" ",end=" ")
			columnindex += 1
		print("")
		rowindex +=1
	#print("")
	
	#Second section
	#print("")
	rowindex = 1
	while rowindex<=RowLoop:
		columnindex = RowLoop-rowindex+1
		while columnindex>=1:
			print(f"*" , end=" ")
			columnindex -= 1 
			
		columnindex = 1
		while columnindex<=(rowindex):
			print(f" ",end=" ")
			columnindex += 1
		
		columnindex = 1
		while columnindex<=RowLoop:
			if columnindex<=rowindex-1:
				print(f" ",end=" ")
			else:
				print(f"*",end=" ")
			columnindex += 1
		print("")
		rowindex +=1
		
	print("")

elif numprogram==14:
	RowLoop = int(input("Please enter row number:"))
	
	rowindex = 1
	while rowindex<=RowLoop:
		columnindex =1 
		while columnindex<=rowindex:
			if columnindex==1:
				print("0",end=" ")
			else:
				print(f"{(rowindex-1)*(columnindex-1)}",end=" ")
			columnindex +=1
		print("")
		rowindex +=1
	print("")
elif numprogram==15:
	RowLoop = int(input("Please enter row number:"))
	rowindex =1 
	while rowindex<=RowLoop:
		columnindex=1
		while columnindex<=RowLoop:
			if (rowindex ==1 or rowindex== RowLoop or columnindex==1 or columnindex==RowLoop):
				print(f"*",end=" ")
			else:
				print(" ",end=" ")
			columnindex +=1
		print("")
		rowindex +=1
	
elif numprogram==16:
	RowLoop = int(input("Please enter row number:"))
	rowindex =1 
	while rowindex<=RowLoop:
		columnindex=1
		while columnindex<=RowLoop:
			if (rowindex ==1 or rowindex== RowLoop or columnindex==1 or columnindex==RowLoop or columnindex == rowindex or columnindex == (RowLoop-rowindex+1)):
				print(f"*",end=" ")
			else:
				print(" ",end=" ")
			columnindex +=1
		print("")
		rowindex +=1
	