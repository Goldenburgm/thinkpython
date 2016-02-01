s1 = int(raw_input("What's the size of stick one?\n"))
s2 = int(raw_input("What's the size of stick two?\n"))
s3 = int(raw_input("What's the size of stick three?\n"))

def is_triangle():
	if ((s1 > s2 + s3) or (s2 > s3 + s1) or (s3 > s2 + s1)):
		print "You can't make a triangle with these!"
	else:
		print "You can make a triangle!"

is_triangle()				