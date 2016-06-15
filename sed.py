#!/usr/bin/python

import sys

def sed(pattern, rep, file1, file2):
	"""
	pattern, rep: string
	file1, file2: files
	Writes file2 using the contents of file1, replacing given pattern by
	given rep (replacement).
	"""
	try:
		open_file1 = open(str(file1), 'r')
	except:
		print "File does not exist."
		sys.exit(1)

	open_file2 = open(str(file2), 'w')

	for line in open_file1:
		if pattern in line:
			words = line.split()
			res = [word.replace(pattern, rep) for word in words]
			open_file2.write(" ".join(res))
			open_file2.write("\n")
		else:
			open_file2.write(line)		

if __name__ == "__main__":
	#ignoring script name as argument
	try:
		sed(*sys.argv[1:])
	except TypeError:
		print "Not enough arguments. Usage: sed.py pattern replacement source",
		print "file1 file2"
		
