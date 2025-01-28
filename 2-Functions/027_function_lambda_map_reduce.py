"""
reduce() function:
It is not directly available , we need import functool module
Apply a perticular function inits first argument position
reduce will extract 1st two elements at a time 

Syntax:
reduce(InFuncitonName,sequence)
"""

import os
os.system("cls")
import functools

myPrices =[10,50,23,67,89,45,34]
print(f"\nInput dict list  is : {myPrices}")
#It is will first 10, 50 and store 60 value in the memory
#60 will come as first value and it will take 23 value as 2nd value  total 83 will be kept in the memory
total = functools.reduce(lambda myprice01,myprice02: myprice01+myprice02,myPrices)
print(f"\n Final total is : {total}")