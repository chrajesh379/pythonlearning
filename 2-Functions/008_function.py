"""
keyward arguments are passed to a function as Key - Value pairs
These will be represented as **kwargs. These arguments are collected as Dictionary 
Keys are represented as Argument Names
Values are represented as Argument Values

"""
import os
from tabulate import tabulate
os.system("cls")

def buildprofile(**kwargs):
	profiledata = {}
	
	profiledata["FirstName"] = kwargs.get("FirstName","Not Given")
	profiledata["LastName"] = kwargs.get("LastName","Not Given")
	profiledata["Age"] = kwargs.get("Age","Not Given")
	profiledata["Height"] = kwargs.get("Height","Not Given")
	profiledata["Place"] = kwargs.get("Place","Not Given")
	profiledata["Phone"] = kwargs.get("Phone","Not Given")
	profiledata["Email"] = kwargs.get("Email","Not Given")
	
	print("\nRegistered user information is: \n ")
	for outKey,outName in profiledata.items():
		print(f"{outKey} : {outName}")

buildprofile(FirstName = "Rajesh" , LastName = "c" , Age = 36 , Height = 5.7 , Place = "Bangalore" ,  Phone = "987654321" , Email = "abc@gmail.com"  ) 
buildprofile(FirstName = "Rajesh" , LastName = "c" , Age = 36 , Height = 5.7  ) 
buildprofile(FirstName = "Rajesh" , Place = "Bangalore" ,  Phone = "987654321" , Email = "abc@gmail.com"  ) 