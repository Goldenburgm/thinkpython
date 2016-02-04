def read_words():
	"""
	Checks every line in file words.txt and prints
	the ones that are over 20 characters
	"""
	fin = open("words.txt")
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word

read_words()			
