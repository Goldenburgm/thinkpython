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
	"""
	Same traversal function, this time using a for loop.
	"""
	for char in string:
		print char	

def traversal_for_reversed(string):
	"""
	Reversed string traversal function, using a for loop.
	"""
	index = len(string) - 1
	for char in string:
		char = string[index]
		print char			
		index -= 1

def ducklings():
	"""
	Prints ducks' names in alphabetical order. 
	"""
	prefixes = "JKLMNOPQ"
	suffix_ack = "ack" 
	suffix_uack = "uack" #some of these ducks have different suffixes in their names
	for letter in prefixes:
		if letter == prefixes[5] or letter == prefixes[7]:
			print letter + suffix_uack 
		else:
			print letter + suffix_ack	

def test(string):
	testing = string[:] 
	print testing #returns the whole string

def find(word, letter, index):
	"""
	Finds given letter in the given word.
	"""
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1

def find_and_count(word, letter):
	"""
	Returns how many times a letter is in a word
	"""			
	index = 0
	count = 0
	while index < len(word):
		if letter == word[index]:
			count += 1
		index += 1
	return count	

def find_and_count_for(word, letter):
	"""
	Find and count using a for loop.
	"""		
	index = 0
	count = 0
	for char in word:
		if letter == word[index]:
			count +=1
		index += 1
	return count		

def find_and_count_2(word, letter):
	"""
	"""
	index = 0
	count = 0
	for char in word:
		if find(word, letter, index) == index:
			count += 1
		index += 1
	return count		

print find_and_count_2("banana", "a")