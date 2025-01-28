"""
"""
import os
os.system("cls")

def counterGenerator():
	counter =0
	def getCounter():
		nonlocal counter
		counter += 1
		return counter
	return getCounter

if __name__ =="__main__":
	counterSequence = counterGenerator()
	for index in range(10):
		print(f"sequence is {counterSequence()}")