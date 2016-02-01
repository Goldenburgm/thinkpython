import random
import math

def newton_sqrt(a, x):
	"""Takes two float numbers:
		calculates the square root of a,
		using the estimative x
	   This function iterates the value of x
	   through the formula, then assigns the result to x.
	   The iteration stops when the estimative stops changing.	
	"""
	epsilon = 0.00000000001
	while True:
		print x, #prints the estimative for each iteration
		y = (x + a/x) / 2 
		if abs(y-x) < epsilon: #if the absolute value of y - x is less than 0.00001
			break   		   #it breaks out of the loop	
		x = y #sets the result as the next estimative	

def square_root(a):
	"""Takes int a and randomly chooses a reasonable number x,
	based on the square root of a, testing it in Newtons 
	function. 
	PS.: Sometimes it chooses the right square root.
	"""
	x = random.randint(int(math.sqrt(a)-2),int(math.sqrt(a)+2))
	newton_sqrt(a, x)	


newton_sqrt(9, 26)


			
