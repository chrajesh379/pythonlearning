"""
map() - map function executes specific function for each item passed from the iteratable object

Syntax:
map(function,iteratable1,[iteratable2....iteratablen])
return value is always map and using collection like list or tuple, we can extract data.

generate squares for list of elements
"""

import os
os.system("cls")

mylist=[1,2,3,4,5,6]
print(f"\nOriginal list is : {mylist}")
squares = list(map(lambda x:x*x,mylist))
print(f"\nsquares list is : {squares}")