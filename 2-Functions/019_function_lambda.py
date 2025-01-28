"""
find squares and cubes

"""

import os
os.system("cls")

findsquare = lambda x : x*x
findcube = lambda x : x * findsquare(x)

num1 = int(input("Please enter number 1 "))
choice = int(input("Please enter the choice\n 1.Square and 2. Cube \n"))
if choice ==1:
	print(f"\nSquare of the number {num1} is {findsquare(num1)}")
elif choice ==2:
	print(f"\nCube of the number {num1} is {findcube(num1)}")