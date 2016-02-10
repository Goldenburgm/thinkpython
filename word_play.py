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

