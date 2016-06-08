import string
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
		if i < (len(t) - n):
			suffix = t[i+n]
		else:
			break
		prefix = " ".join(t[i:(i+n)])
		res.setdefault(prefix, []).append(suffix)
		i += 1
	return res

if __name__ == "__main__":
	book = wfa.file_to_word_list("pg41787.txt")
	markov_dict = markov_analysis(book, 2)
	for key, val in markov_test.items():
		print key, r.choice(val),




