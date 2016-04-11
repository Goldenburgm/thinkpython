"""Exercises from book Think Python, by Allen B. Downey.
http://thinkpython.com
Following code by Matheus Fernandes Gonçalves,
04/10/2016.
"""

def file_to_dict(file):
	"""Receives: file
	   Returns: dict
	   Converts each line of a file to a key in a dict.
	   Obs: values are integers.
	"""
	res = dict()
	i_value = 0
	open_file = open(str(file))
	for line in open_file:
		raw_line = line.strip()
		res[raw_line] = i_value
		i_value += 1
	return res

print "zymurgy" in file_to_dict("words.txt")		
