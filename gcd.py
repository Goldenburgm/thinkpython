def gcd(a, b):
	if b == 0:
		return a
	elif a == 0:
		return b
	else:
		return gcd(b, a % b) 	


print gcd(4, 3) 
