def print_n(s, n): 
	"""Takes a string s
	and print it n times
	"""
	if n <= 0:
		return
	print s
	print_n(s, n-1)

def countdown(n):
	"""Takes a number n and starts to count down.
	When the number reaches zero, print 'Blast off!'
	"""
	if n <= 0:
		print "Blast off!"
	else:	
		print n
		countdown(n-1)	

def do_n(f, n):
	"""Takes a function f and a number n.
	Calls the given function n times
	"""
	if n <= 0:
		return
	if f == countdown:
		countdown(10)
	else:
		print_n("Hello", 3)	



do_n(print_n, 1)