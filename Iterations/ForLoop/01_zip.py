"""
1. The Zip() function is a built in function in Python Namespace
2. Zip function accepts "Iteratable Objects " OR "Container Objects" as an Arguments and returns A "Single Iterator Object"
3. The returned "Single Iterator Object" will be Having Mapped values from All the Containers that are Supplied
4. zip() built in function is mostly used to "Map Similar Index of Multiple Containers" to be Handled as a "Single Entity"
5. zip() by default return address location of the iterator . we have to iterate through object
Basic Syntax:
zip(*iteratorObjects)
"""

import os
os.system("cls")

print("illustration of Zip Function")
print("-------------------------------")

itemsInBasket =["Scissiors","Paper Packs","Glue Sticks","Staple Pins"]
itemsQuantity =[10,25,15,20,5]
print("Mapping The items with Quantity\n")

finalbasket = zip(itemsInBasket,itemsQuantity)
print(f"zip direct value {finalbasket}\n")

# We are iterating the Zip object though list to get the values
print(f"zip direct value {list(finalbasket)}\n")

for itemname,quantity in zip(itemsInBasket,itemsQuantity):
	print(f"The {itemname} with purchased quantity : {quantity}")
	
