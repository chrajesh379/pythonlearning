"""
Write a program to generate arthematic progression
Difference is common
EX: 2,5,8,11,14
arthemicprograa(1,14,3) and (14*3)-3+1
arthemicprograa(1,13,3) and (13*3)-3+1
...
...
etc
"""

import os
os.system("cls")

def arthemicprograa(startNum,endRange,commonDiff):
	if startNum == endRange:
		print(1,end=" ")
	else:
		arthemicprograa(startNum,endRange-1,commonDiff)
		print((endRange*commonDiff)-commonDiff+1,end=" ")
	

startNum = int(input("Please Enter the Start Number : "))
commonDiff = int(input("Please Enter the Common Difference : "))
endRange = int(input("Please Enter the End Range : "))

for i in range(startNum,endRange*commonDiff,commonDiff):
	print(i,end=" ")
print("")
arthemicprograa(startNum,endRange,commonDiff)