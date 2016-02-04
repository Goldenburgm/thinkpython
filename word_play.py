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
	
		




read_words()		
