"""
Any problem that can be represented from Nth Order to N-1 th order

Write a program to generate a Sequential seris 
"""

import os
os.system("cls")

def seqSeries(startSeries,endSeries):
	if startSeries>endSeries:
		return
	else:
		print(startSeries)
		seqSeries(startSeries+1,endSeries)
		
def naturalNumbers(startrangeNatural):
	if startrangeNatural<1:
		print(startrangeNatural)
	else:
		naturalNumbers(startrangeNatural-1)
		print(startrangeNatural)

		
startSeries = int(input("Please Enter start range: "))
endSeries = int(input("Please Enter End range: "))
naturalNumbersRange = int(input("Please Enter natural Numbers Range: "))
print("Sequence Numbers : ")
seqSeries(startSeries,endSeries)
print("Natural Numbers : ")
naturalNumbers(naturalNumbersRange)
