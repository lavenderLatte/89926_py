"""
Create a python module helperfunctions.py with the following functions.
add - returns the sum of two numbers
diff - returns the difference between two numbers
product - returns the product of two numbers
greatest - returns the greatest of two numbers.
Import this module in your python program and use the functions your created on any two numbers and print the result.
"""

def add(a, b):
	return a + b

def diff(a, b):
	return a - b

def product(a, b):
	return a * b

def greatest(a, b):
	if a >= b:
		return a
	else:
		return b

