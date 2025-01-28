"""
Given a list of strings, find all palindromes.
"""

import os
os.system("cls")

my_list = ["geeks", "geeg", "keek", "practice", "aa"] 
print(f"Original list is : {my_list}")
palindrome = list(filter(lambda value: (value == value[::-1]), my_list))
print(f"\npalindrome list is : {palindrome}")