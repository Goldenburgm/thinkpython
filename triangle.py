def is_triangle(s1, s2, s3):
	"""Takes three sticks as arguments.
	If any of the sticks is greater than the
	sum of the other two, it can't form a
	triangle, so it returns 'no!'
	"""
	if ((s1 > s2 + s3) or (s2 > s3 + s1) or (s3 > s2 + s1)):
		print "No!"
	else:
		print "Yes!"

is_triangle(1, 10, 10)		