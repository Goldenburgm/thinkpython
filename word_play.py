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
	the ones that have no e, and the percentage
	of words without the e character
	"""
	file_words = open("words.txt") #opening the file words.txt and assigning it to file_words
	lines = 0 #starting lines count
	no_e_count = 0 #starting lines without e count
	for line in file_words:
		lines += 1 #counts every line in the file
		word = line.strip() #removes empty spaces from each line
		if has_no_e(word) == True:
			print word
			no_e_count += 1 #counts every line without e in the file
	percentage = (float(no_e_count) / float(lines)) * 100 
	print "%d percent of the words have no e!"	%(percentage)	
	
		
def avoids(word, f):
	"""
	word: string
	f: string

	Receives a word and checks if it contains any character in
	string f. If it doesn't, it returns True. 
	"""
	for char in f:
		if char in word:
			return False
	return True			


def has_no_sub():
	"""
	sub: string

	Checks how many words in words.txt don't have any of the
	characters in string sub, and prints them on the screen.
	"""	
	file_words = open("words.txt")
	count = 0
	count_lines = 0
	sub = raw_input("> ")
	for line in file_words:
		count_lines += 1
		word = line.strip()
		if avoids(word, sub) == True:
			print word
			count += 1			
	percent = (float(count) / float(count_lines)) * 100.0
	print "%s words don't have any of the characters in %s" %(count, sub)	
	print "%f percent of words don't have any of the characters in %s" %(percent, sub)

def uses_only(word, sub):
	"""
	word: string
	sub: string

	Tests if string word uses only the characters in string sub.
	"""
	for char in word:
		if char not in sub:
			return False	
	return True

def uses_only_sub():
	"""
	sub: string

	Checks every word in words.txt and returns only the ones that
	use only the characters in sub.
	"""
	sub = raw_input("> ")
	file_words = open("words.txt")
	for line in file_words:
		words = line.strip()
		if uses_only(words, sub) == True:
			print words

def uses_all(word, sub):
	"""
	word: string
	sub: string

	Tests if the string word uses all the characters in string sub
	(no particular order), returning true if it does.
	"""
	for char in sub:
		if char not in word:
			return False	
	return True

def uses_all_sub():
	"""
	sub: string

	Checks every word in words.txt and prints each word that uses
	all the characters in string sub.
	"""
	file_words = open("words.txt")
	count = 0
	sub = raw_input("> ")
	for line in file_words:
		words = line.strip()
		if uses_all(words, sub) == True:
			print words
			count += 1
	print "%d words use all the letters in '%s'" %(count, sub)		

def is_abecedarian(word):
	"""
	word: string

	Tests if given word is abecedarian, returning True if it is.
	"""
	last_char = ord(word[0])
	for char in word:
		current_char = ord(char)
		if current_char < last_char:
			return False
		last_char = current_char
	return True		

def abecederian_words():
	"""
	Checks how many words in words.txt are abecedarian.
	"""	
	file_words = open("words.txt")
	count = 0
	for line in file_words:
		word = line.strip()
		if is_abecedarian(word) == True:
			print word
			count += 1
	print "%d words are abecedarian." %(count)	

def three_double_letters(word):
	"""
	word: string

	Checks if given word has three consecutive double letters.
	"""
	i = 0
	three_doubles = 0
	while i < len(word) - 1:
		if word[i] == word[i+1]:
			three_doubles += 1
			i += 2
			if three_doubles >= 3:
				return True
		else:
			three_doubles = 0
			i += 1
	return False		


		
				
	
def check_three_double_letters():
	"""
	Searches for words in words.txt that have 3 consecutive
	double letters and prints them.
	"""	
	file_words = open("words.txt")
	for line in file_words:
		word = line.strip()
		if three_double_letters(word) == True:
			print word







check_three_double_letters()


			
