import string as s
import operator as op

def file_word_frequency(f):
	"""f: file
	Returns a list where each item is composed of a word and
	the frequency of that word in given file. Ignores punctuation and
	uppercase.
	"""
	t = dict()
	open_file = open(f)
	for line in open_file:
		for item in line.split():
			word = "".join([char.lower() for char in item if 
							char not in s.punctuation])
			t[word] = t.get(word, 0) + 1
	res = [(word, freq) for (word, freq) in t.items()]	
	res.sort(reverse=True, key=op.itemgetter(1))
	return res

	
if __name__ == "__main__":
	for item in file_word_frequency("pg41787.txt"):
		print item[0], item[1]
	