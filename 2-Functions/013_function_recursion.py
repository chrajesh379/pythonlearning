"""
Write a program to generate 1/1! + 2/2! + 3/3! + 4/4! + 5/5!

5/5!+calculateSeries(4)
5/5!+4/4!+calculateSeries(3)
5/5!+4/4!+3/3!+calculateSeries(2)
5/5!+4/4!+3/3!+2/2!+calculateSeries(1)
5/5!+4/4!+3/3!+2/2!+1
"""

import os
os.system("cls")

def factorial(seriesLevel):
	if seriesLevel==0:
		return 1
	else:
		return seriesLevel*factorial(seriesLevel-1)

def calculateSeries(seriesLevel):
	SeriesSum = 0
	#x = seriesLevel /factorial(seriesLevel)
	if seriesLevel == 1:
		return 1
	else:
		return (seriesLevel/factorial(seriesLevel))+(calculateSeries(seriesLevel-1))


seriesLevel = int(input("Please Enter the Series Level : "))
print(f"Series level {seriesLevel} is : {calculateSeries(seriesLevel)}")
print(f"factorial of a number {seriesLevel} is : {factorial(seriesLevel)}")