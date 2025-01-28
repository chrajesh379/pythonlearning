"""

reduce can't work for multiple sequences
"""

import os
os.system("cls")
import functools

myPrices = [25,19,35,16,45,28,32,15,8,26]
myTaxes=[8,5,15,2,12,20,10,17,25,9]
print(f"\nInput myPrices list  is : {myPrices}")
print(f"\nInput myTaxes list  is : {myTaxes}")

finalList = list(map(lambda price,tax : (price*tax),myPrices,myTaxes))
print(f"\nFinal list  is : {finalList}")
TotalPrice = functools.reduce(lambda price1,price2:(price1+price2),finalList)
print(f"\nTotalPrice is : {TotalPrice}")
# or

TotalPrice_1 = functools.reduce(lambda price1,price2 :  price1+ price2, [myPrices*myTaxes for myPrices,myTaxes in zip(myPrices,myTaxes)])
print(f"\nTotalPrice_1 is : {TotalPrice_1}")