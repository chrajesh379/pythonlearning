"""
running total of all the items price
"""
import os
from tabulate import tabulate
os.system("cls")

def price_detail(*args):
	listprices_out = []
	running_total = 0
	for priceid,price in enumerate(args,start=1):
		running_total += price
		listprices_out.append([priceid,price,running_total])
	print(tabulate(listprices_out,headers=["priceid","price","running_total"],stralign='right',tablefmt = "pretty", floatfmt = "0.2f"))

price_detail(10,20,15,25,20,30,40)