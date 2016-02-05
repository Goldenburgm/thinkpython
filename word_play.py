def has_no_e(word):
	"""
	Returns true if the given word has no e. 
	"""			
	for char in word:
		if char == "e":
			return False
	return True	

def read_words():
	"""
	Checks every line in file words.txt and prints
	the ones that are over 20 characters
	"""
	file_words = open("words.txt")
	lines = 0
	no_e_count = 0
	for line in file_words:
		lines += 1
		word = line.strip()
		if has_no_e(word) == True:
			print word
			no_e_count += 1
	percentage = (float(no_e_count) / float(lines)) * 100
	print "%d percent of the words have no e!"	%(percentage)	
	
		
def avoids(word, f):
	"""
	word: string
	f: string

	Receives a word and checks if it doesn't contain string
	f. If it doesn't, it returns True. 
	"""

	if f.upper() in word.upper():
		return False
	return True	

def has_no_sub(sub):
	"""
	sub: string

	Checks how many words in words.txt have no string 
	sub
	"""
	




print avoids("Python", "pyti")
