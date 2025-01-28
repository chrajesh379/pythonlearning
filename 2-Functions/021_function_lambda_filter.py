"""
filter()

filter() function accepts given a sequence of values supplied by collection and filters the required element that satisfies the given condition in the filter function argument

syntax: filter(Condition,sequence)

Extract even number tempatures
"""

import os
os.system("cls")

mytempatures = [25,19,35,16,45,28,32,15,8,26,37,42]
eventemp = list(filter(lambda temp: (temp%2==0),mytempatures))
print(f"even tempartures are: {eventemp}")	

oddtemp = list(filter(lambda temp: (temp%2!=0),mytempatures))
print(f"even tempartures are: {oddtemp}")	

greater25temp = list(filter(lambda temp: (temp>25),mytempatures))
print(f"even tempartures are: {greater25temp}")

templevel = int(input("Please enter the tempature that needs to filter : "))
tempfilter = list(filter(lambda temp: (temp>templevel),mytempatures))
print(f"even tempartures are: {tempfilter}")