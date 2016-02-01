import math
from swampy.Lumpy import Lumpy

def compare(x, y):
	if (x > y):
		return "1"
	elif (x == y):
		return "0"
	else:
		return "-1"

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	squared_xy = math.pow(dx, 2) + math.pow(dy, 2)
	distance = math.sqrt(squared_xy)
	return distance

def hypotenuse(a, b):
	return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

def area(r):
	return math.pi + math.pow(r, 2)

def circle_area(xc, yc, xp, yp):
	return area(distance(xc, yc, xp, yp))

def is_divisible(x, y):
	return x % y == 0

def is_between(x, y, z):
	return x <= y <= z	

def factorial(n):
	if not isinstance(n, int):
		print 'Factorial is only defined for integers'
		return None
	elif n < 0:
		print 'Factorial is not defined for negative integers'
		return None	
	elif n == 0:
		return 1
	else:
		recurse = factorial(n - 1)
		result = n * recurse
		return result	

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)		

def b(z):
	prod = a(z, z)
	print z, prod
	return prod				

def a(x, y):
	x = x + 1
	lumpy.object_diagram()
	return x * y

def c(x, y, z):
	total = x + y + z
	square = b(total) ** 2
	return square

lumpy = Lumpy()
lumpy.make_reference()

x = 1
y = x + 1
print c(x, y + 3, x + y)

