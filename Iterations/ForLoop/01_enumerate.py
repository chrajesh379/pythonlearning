"""
1. Enumerate() function is build in fucntion. That can Enumerate the data values that are extracted from the collection
2. Enumerate() cuntion adds a counter to an iteratable object and returns the Iteratable object as an Enumerating object Allocation one counter value for each element that is extracted.

Basic Syntax
enumerate(IteratorObject,start=0)
"""

import os
os.system("cls")

print("illustration of enumerate Function")
print("-------------------------------")

itemsInBasket =["Scissiors","Paper Packs","Glue Sticks","Erasers","Staple Pins"]
itemsQuantity =[10,25,15,20,5]
itemsPrice =[15.25,100,200,20.56,80]
print("Mapping The items with index values\n")

finalbasket = enumerate(itemsInBasket)
print(f"enumerate direct value {finalbasket}\n")

# We are iterating the Enumerate object though list to get the values
print(f"Enumerate direct value {list(finalbasket)}\n")

for itemIndex,(itemName,itemQuantiy,itemPrice) in enumerate(zip(itemsInBasket,itemsQuantity,itemsPrice)):
	print(f"The {itemIndex} with purchased {itemName} havig quantity {itemQuantiy} and the price is {itemPrice}")