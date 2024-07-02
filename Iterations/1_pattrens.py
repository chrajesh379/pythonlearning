import os
os.system("cls")

print("pattrens program", end="\n")
print("1.number pattren program")
print("Outer Loop will dicate Rows and Inner loop will dicate columns")

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

	rowindex_1 = 1
	spaces = (RowLoop*3)+1
	middle_sapce = (RowLoop*2)
	rowindex_2 = 1
	space=' '
    
	while rowindex_1<=RowLoop:
		#print(f"outerloop iteration level is : {rowindex}")
		columnindex_1 = 1
		while columnindex_1<=rowindex_1:
			#print(f"innerloop iteration level is: {columnindex}")
			print(f"*" , end=" ")
			columnindex_1 += 1 
		print(f"{space*middle_sapce}",end="")
		print("z",end=" ")
		print(f"{space*RowLoop}",end=" ")
		print("y",end=" ")
		print("")
		spaces =spaces-2
		middle_sapce = middle_sapce-2
		rowindex_1 +=1
	print("")