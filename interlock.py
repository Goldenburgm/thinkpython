import bisect
from is_pallindrome_word_list import *

def open_file(f):
	"""
	Receives file f and opens it.
	"""
	global global_file
	global_file = open(f)

def close_file():
	"""
	Closes current open file.
	"""	
	global_file.close()

def file_to_list():
	"""
	Converts open file to a list.
	Obs: list has global access.
	"""	
	global file_list
	file_list = []
	for line in global_file:
		word = line.strip()
		file_list.append(word)

def interlock(word):
	"""
	Receives word. Tests if given word is composed by two
	interlocking words.
	"""
	#checks each even character
	evens = word[::2]
	#checks each odd character
	odds = word[1::2]
	if word_bisect(evens) == True and word_bisect(odds) == True:
		return True
	else:
		return False

def interlock_list():
	"""
	Checks current open file and returns every word that interlocks.
	"""		
	res = []
	for word in file_list:
		if interlock(word) == True:
			res.append(word)
			res.append(word[::2])
			res.append(word[1::2])
	return res		

def three_way_interlock(word):
	"""
	Checks if a word is composed of three interlocked words.
	"""	
	for i in range(3):
		inter = word[i::3]
		if word_bisect(inter) == False:
			return False
	return True		

def three_way_interlock_list():
	"""
	Returns a list of all words that are three way interlocked.
	"""
	res = []
	for word in file_list:
		if three_way_interlock(word):
			res.append(word)
			res.append(word[0::3])
			res.append(word[1::3])
			res.append(word[2::3])
	return res			

open_file("words.txt")
file_to_list()
print three_way_interlock_list()

	