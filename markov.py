import word_frequency_analysis as wfa
import random as r

def markov_analysis(t, n):
	"""t: word list
	n: prefix size
	Performs a markov analysis in given word list. Returns a dict with prefixes as keys and
	possible suffixes as values.
	"""
	res = dict()
	i = 0
	for word in t:
		try:
			suffix = t[i+n]
		except:
			print "Out of range"
		prefix = " ".join(t[i:t.index(suffix)])
		res.setdefault(prefix, []).append(suffix)
		i += 1
	return res

def random_text(d, n=1000):
	"""d: markov dictionary
	n: integer
	Prints a random text using the words in d. The text will be generated in n iterations.
	"""
	i = 0
	while i < n:
		try:
			prefix = suffix
			suffix = r.choice(markov_dict[prefix])
			print prefix, suffix,
			i += 1
		except:
			prefix = " ".join(r.sample(markov_dict, 1))
			suffix = r.choice(markov_dict[prefix])
			print prefix, suffix,
			i += 1
	
book = wfa.file_to_word_list("pg41787.txt")
markov_dict = markov_analysis(book, 2)			

if __name__ == "__main__":
	random_text(markov_dict, 300)			

		


