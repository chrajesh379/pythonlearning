"""
find simple intrest

"""

import os
os.system("cls")

simpleIntrest = lambda inPrinciple,inIntrestRate,inTimeperiod : (inPrinciple * inIntrestRate * inTimeperiod)/100

inPrinciple = int(input("Please enter the principle amount : "))
inIntrestRate = int(input("Please enter the Intrest Rate : "))
inTimeperiod = int(input("Please enter the Timeperiod : "))

print(f"\nSimple Intrest for the principle amount {inPrinciple} with Intrest rate {inIntrestRate} and timeperiod {inTimeperiod} is : ")
print(f"{inPrinciple+simpleIntrest(inPrinciple,inIntrestRate,inTimeperiod)}")