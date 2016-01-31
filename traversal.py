def traversal(string):
	"""
	Traverses each character of the string
	and prints it on the screen.
	"""
	index = 0
	while index < len(string): #while index is smaller than the
		letter = string[index] #length of the string
		print letter, #prints a letter for each iteration
		index += 1 #increments index

def traversal_reversed(string):
	"""
	Starting from the last letter, this 
	function prints each string character
	"""
	index = len(string)
	while index > 0:
		letter = string[index-1]
		print letter
		index -= 1		

def traversal_for(string):
	for char in string:
		print char	

def traversal_for_reversed(string):
	for char in string:
		print char			

traversal_for_reversed("banana")