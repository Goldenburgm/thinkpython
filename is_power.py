def is_power(a, b):
	if a == 1:
		return True
	elif a%b == 0 and is_power(a/b, b) == True:
		return True
	else:
		return False

print is_power(27, 3)			
