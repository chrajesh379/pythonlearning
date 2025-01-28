"""
map with multiple iteratable 

"""

import os
os.system("cls")

numbers1 = [2, 4, 5, 6, 3]
numbers2 = [1, 3, 2, 2, 4]
print(f"\nOriginal list numbers1 is : {numbers1}")
print(f"\nOriginal list numbers2 is : {numbers2}")
finallist = list(map(lambda x,y : x+y,numbers1,numbers2))
print(f"\nfinal list is : {finallist}")

myprices =[55,24,32,67,17,73]
taxes =[8,3,5,9,2,12]
print(f"\nOriginal list myprices is : {myprices}")
print(f"\nOriginal list taxes is : {taxes}")
finalprice = list(map(lambda x,y : x+y,myprices,taxes))
print(f"\nfinalprice list  is : {finalprice}")