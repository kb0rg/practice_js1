"""
example python code to translate into JS
"""

def sum_mult(n):
	sum = 0
	for i in range(n):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	print sum

sum_mult(1000)