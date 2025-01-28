"""
Given a list of strings and a string str, print all anagrams of str

"""

import os
os.system("cls")

my_list = ["geeks", "geeg", "keegs", "practice", "aa"] 
print(f"\nOriginal list is : {my_list}")
input_str = input("Please enter the input string: ")
anagram = list(filter(lambda value : (sorted(input_str)==sorted(value)),my_list))
print(f"\nanagram list is : {anagram}")