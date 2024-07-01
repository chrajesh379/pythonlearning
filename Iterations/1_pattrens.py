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