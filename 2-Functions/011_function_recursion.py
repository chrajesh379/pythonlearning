"""
write a proagram to find the power of give number, raised to a given number
"""

import os
from tabulate import tabulate
os.system("cls")

def powernum(powerNumber,inputNumber):
	if inputNumber==1:
		return powerNumber
	else:
		return powerNumber * powernum(powerNumber,inputNumber-1)
		

powerNumber = int(input("Please enter the Power Number :"))
inputNumber = int(input("Please enter the Number :"))

print(powernum(powerNumber,inputNumber))