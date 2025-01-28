"""

Maximum and minimum element from the list
"""

import os
os.system("cls")
import functools

myList =[1,4,6,10,23,56,10,22]
print(f"\nInput myList list  is : {myList}")
maxValue = functools.reduce(lambda x,y : (x if x>y else y),myList)
print(f"\nmaxValue is : {maxValue}")
minValue = functools.reduce(lambda x,y : (x if x<y else y),myList)
print(f"\nminValue is : {minValue}")