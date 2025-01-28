"""
Factorial

5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 * 0
"""
import os
os.system("cls")

def factioral_closure():
	cache ={}
	def factorial(n):
		if n in cache:
			print(f"cahce is {n}")
			print(f"cache actual value is  is {cache}")
			return cache[n]
		else:
			print(f"cahce not exists {n}")
			print(f"cache actual value is  is {cache}")
			if n==0:
				result= 1
			else:
				result = n * factorial(n-1)
				print(f"result is {result}")
				#cache[n] = result
			cache[n] = result
			return result
	return factorial




if __name__=="__main__":
	fact = factioral_closure()
	factInput = int(input("Please Enter factInput Value: "))
	print(fact(factInput))
	factInput = int(input("Please Enter factInput Value: "))
	print(fact(factInput))