"""
Employees with a performance rating of 5 will receive a 10% bonus.
Employees with a performance rating of 4 will receive a 5% bonus.
Employees with a performance rating of 3 or below will not receive a bonus.

"""

import os
os.system("cls")

employees = [
    {"name": "Alice", "salary": 50000, "performance_rating": 5},
    {"name": "Bob", "salary": 60000, "performance_rating": 4},
    {"name": "Charlie", "salary": 55000, "performance_rating": 3},
    {"name": "David", "salary": 70000, "performance_rating": 2}
]
print(f"\nInput dict list  is : {employees}")
finallist = list(map(lambda emp : (emp["salary"]*0.10 if emp["performance_rating"]==5 else  emp["salary"]*0.05 if emp["performance_rating"]==4 else emp["salary"]),employees))
print(f"\nfinallist list  is : {finallist}")
