import math

def newtons(a, x):
	"""
	Receives estimative x and attempts to compute 
	the square root of a. Each iteration gets closer
	to the result. If the result stops changing, 
	it breaks out of the loop.
	"""
	epsilon = 0.000000000001
	while True:
		#print x #prints estimative
		y = (x + a/x) / 2 #newtons method to compute square roots
		if abs(y-x) < epsilon: 
			break #breaks out of the loop if the estimatives stop changing
		x = y
	return y		

def test_sqrt():
	"""
	Compares the results of our newtons() function
	with the results of the built in math.sqrt 
	python function. Computes the square roots from
	1 to 9;
	"""	
	x = 1	
	while x < 10:
		print "Square root of %d:" %(x), 
		print newtons(x, math.sqrt(x)),
		print math.sqrt(x),
		print abs(newtons(x, math.sqrt(x)) - math.sqrt(x))
		x += 1

test_sqrt()

