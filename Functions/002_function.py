"""
This is called positional notation: op1 is mapped to in_op1 and op2 mapped in_op2 and operation_type mapped to in_operation_type
def operation(in_op1,in_op2,in_operation_type)
                ^  ^      ^
				|  |      |
		        |  |      |
    operation(op1,op2,operation_type)
	
if you want to use names insted then it is named notation or keyward notation 

def operation(in_op1,in_op2,in_operation_type)

	operation(in_op2=op2,in_op1=op1,in_operation_type=operation_type)

"""

import os
os.system("cls")

def operation(in_op1,in_op2,in_operation_type):
	if operation_type=="+":
		return (op1+op2)
	elif operation_type=="-":
		return (op1-op2)
	elif operation_type=="*":
		return (op1*op2)
	elif operation_type=="/":
		if op2==0:
			return 0
		else:
			return (op1/op2)
	elif operation_type=="%":
		if op2==0:
			return 0
		else :
			return (op1%op2)
			


op1 = int(input("please enter first value: "))
op2 = int(input("\nplease enter second value: "))		
operation_type = input("\nplease enter operation_type value either +,-,*,/,%: ")	
#result = operation(op1,op2,operation_type)
result = operation(in_op2=op2,in_op1=op1,in_operation_type=operation_type)
print(f"\nresult is {result}")