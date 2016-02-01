import math

<<<<<<< HEAD
pi = math.pi

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def estimate_pi():
	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4*k) * (1103 + 26390*k)
		den = factorial(k) ** 4 * 396 ** (4 * k)
		term = factor * num / den
		total += term
		if abs(term) < 1e-15:
			break
		k += 1
	return 1 / total
	return k
print estimate_pi()
print pi

=======
def factorial(n): 
	"""
	Computes the factorial of n.
	"""
	if n == 0: 
		return 1 
	else:
		return n * factorial(n-1)
			

def estimate_pi():
	"""
	Computes an estimate of pi,
	according to Srinivasa Ramanujan's 
	formula. 
	"""
	factor = 2 * math.sqrt(2) / 9801
	k = 0
	total = 0
	while True:
		num = factorial(4*k) * (1103+26390*k)
		den = factorial(k) ** 4 * 396 ** (4*k)
		term = factor * num / den
		total += term
		if abs(term) < 1e-15: 
			break
		k += 1					
	return 1 / total

print estimate_pi()	
print float(math.pi)	
>>>>>>> 4c16cca8ceafed2d564ccf5b56e9c16d63e4932d
