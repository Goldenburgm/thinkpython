"""Exercises from book Think Python, by Allen B. Downey.
http://thinkpython.com
Coding = UTF-8
Following code by Matheus Fernandes Goncalves,
04/11/2016.
"""

def histogram(s):
	"""Receives string s and returns a histogram with each character in it and
	its respective counters.
	"""
	histogram = dict()
	for item in s:
		#dict get function to make this code more concise.
		#it returns the current occurrences of item in
		#the histogram
		histogram[item] = histogram.get(item, 0) + 1
	return histogram	

def print_hist(h):
	"""Receives dictionary h and returns each key and its corresponding
	value, in ascending order.
	"""
	#converting the keys of dict h into a list
	key_list = h.keys()
	#sorting the key list
	key_list.sort()
	for item in key_list:
		print item, h[item]

		



print_hist(histogram("zab"))

