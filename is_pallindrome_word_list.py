import bisect

def file_list(file_arg):
	"""
	Receives a file and converts it into a list.
	"""	
	global file_list
	file_list = []
	open_file = open(str(file_arg))
	for line in open_file:
		item = line.strip()
		file_list.append(item)	

def word_bisect(s):
	"""
	Returns True if given word is in the words.txt file, using the bisect() function.
	"""	
	b_right = bisect.bisect_right(file_list, s)
	b_left = bisect.bisect_left(file_list, s)
	if b_right > len(file_list) - 1:
		return False
	elif b_left < 0:
		return False
	else:
		if file_list[b_right] == s or file_list[b_left] == s:
			return True
	return False

	
def reverse_pair():
	"""
	Finds all the reverse pairs in the file words.txt 
	and returns a list containing them.
	"""
	res = []
	for i in file_list:
		reverse_word = i[::-1]
		if word_bisect(reverse_word) == True:
			res.append(reverse_word)
			res.append(i)
	return res		
			
file_list("words.txt")			
print reverse_pair()