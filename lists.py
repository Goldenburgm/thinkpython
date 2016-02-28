nested_list = [1, [1, 1, 1], [1, 1, 1, 3]]
nested_string_list = ["a", ["a", "b", "c"], "d"]
cumulative = [1, [1, 1], 3]

def nested_sum(l):
	"""
	Receives list l, and sums all its elements, including
	nested lists.
	"""
	total = 0
	for x in l:
		if type(x) != list:
			total += x
		else:
			total += sum(x)
	return total

def capitalize_all(l):
	"""
	Receives list l and for each element that is a String,
	it will return a capitalized version of it.
	"""	
	result = []
	for s in l:
		for s in s:
			result.append(s.capitalize()) 
	print result

def cumulative_sum(l):
	"""
	Receives a list and return its cumulative sum (works
	with nested lists).
	"""
	result = []
	total = 0
	for x in l:
		if type(x) == list:
			total += sum(x)
			result.append(total)
		else:
			total += x
			result.append(total)	
	print result		

cumulative_sum(cumulative)	





	
		

