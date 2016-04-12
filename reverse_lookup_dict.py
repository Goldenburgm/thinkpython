"""Exercises from book Think Python, by Allen B. Downey.
http://thinkpython.com
Following code by Matheus Fernandes Goncalves,
04/11/2016.
"""

import histogram

test_dictionary = histogram.histogram("aaabbb")

def reverse_lookup(v, d):
	"""v: any value.
	   d: dictionary.
	   Searches for value v in dictionary d. Returns a list with each 
	   corresponding key found.
	"""
	result = []
	for key in d:
		if d[key] == v:
			result.append(key)
	return result

def invert_dict(d):
	"""d: dictionary.
	Returns inverted dictionary (shifts values for keys).
	"""
	result = dict()
	for key in d:
		value = d[key]
		if value in result:
			result[value].append(key)
		else:
			result[value] = [key]	
	return result
	
print invert_dict(test_dictionary)		 
