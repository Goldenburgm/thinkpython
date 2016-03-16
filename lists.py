nested_list = [1, [1, 1, 1], [1, 1, 1, 3]]
nested_string_list = ["a", ["a", "b", "c"], "d"]
cumulative = [1, [1, 1], 3]
t = [1, 3, 5, 7, 8]

def nested_sum(l):
	"""
	Receives list l, and sums all its elements, including
	nested lists. Returns: integer.
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
	it will return a capitalized version of it. Returns:
	new list.
	"""	
	result = []
	for s in l:
		for s in s:
			result.append(s.capitalize()) 

def cumulative_sum(l):
	"""
	Receives a list and return its cumulative sum (works
	with nested lists). Returns: new list.
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
	return result

def middle(l):
	"""
	Receives a list and returns a new one containing all the items
	except the first and last one. Returns: new list.
	"""	
	result = []		
	for i in range(1, len(l) - 1):
		result.append(l[i])
	return result

def chop(l):
	"""
	Removes the first and last items from list l. Returns: none.
	"""		
	del l[len(l) - 1]
	del l[0]

<<<<<<< HEAD
def is_sorted(l):
	"""
	Receives list l and returns true if it is in crescent order.
	"""
	i = 0
	while i < (len(l) - 1):
		if l[i] > l[i+1]:
			return False
		i += 1	
	return True		

def is_anagram(s1, s2):
	"""
	Receives two strings and returns true if they're anagrams.
	"""	
	#Listing both strings
	s1_listed = list(s1)
	s2_listed = list(s2)

	#Capitalizing both listed strings
	s1_capitalized = capitalize_all(s1_listed)
	s2_capitalized = capitalize_all(s2_listed)

	#Sorting both listed strings
	s1_capitalized.sort()
	s2_capitalized.sort()

	if s1_capitalized == s2_capitalized:
		return True
	return False
			
is_anagram("Joe", "OJe")	




	
		

