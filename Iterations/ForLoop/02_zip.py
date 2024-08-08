import os
os.system("cls")
from itertools import zip_longest

print("illustration of Zip Function")
print("-------------------------------")

print("\n single iteratir object\n")
a = [1, 2, 3]
print(list(zip(a)))
print("-------------------------------")
print("\nEqual Length iteratable objects\n")
s={1,2,3}
s1={'a','b','c'}
print(list(zip(s,s1)))
print("-------------------------------")
print("\n UnEqual Length iteratable objects\n")
print("\n In these cases, the number of elements that zip() puts out will be equal to the length of the shortest iterable\n")
print(list(zip(range(5), range(100))))
print("-------------------------------")
print("\n UnEqual Length iteratable objects with longest values\n")
print(list(zip_longest(range(5), range(100),fillvalue='?')))