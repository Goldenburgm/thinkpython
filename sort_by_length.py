import random as rand

def sort_by_length(*args):
	"""Takes given words and returns a new list of words sorted by
	length. Ties are broken at random (words with same length).
	"""
	lengths = list()
	words = list()
	for word in args:
		lengths.append(len(word))
		words.append(word)

	#removing repeated lengths
	lengths = list(set(lengths))

	#sorting lengths and shuffling words
	lengths.sort(reverse=True)
	rand.shuffle(words)

	res = list()
	for length in lengths:
		for word in words:
			if len(word) == length:
				res.append(word)						
	return res
	
print sort_by_length("AAAAAAAAAAAA", "BBBBBB", "CCCCCC")		

