"""
table format data
"""
import os
from tabulate import tabulate
os.system("cls")

def shoppingcart(incartName,*args):
	print(f"Displaying the details of Shopping Cart: {incartName} ")
	outTable = [ [cartid,cartname] for cartid,cartname in enumerate(args,start=1)]
	print("out table is :")
	print(tabulate(outTable,headers=["Item Id","Item Name"],tablefmt="pretty",stralign="left"))

print("Shopping cart 1 \n")
shoppingcart("Shopping Cart 1","Biscuits","Chocolates","Cookies","Juices")
print("Shopping cart 2 \n")
shoppingcart("Shopping Cart 2","Pencils","Pens","Erases","Papers","Cloths")
print("Shopping cart 3 \n")
shoppingcart("Shopping Cart 3","Banana","Apples","Grapes","Guva","Orange","Cherries")