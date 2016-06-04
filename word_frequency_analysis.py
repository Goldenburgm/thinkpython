import string
import operator

def file_to_word_list(f):
	"""f: txt file containing any kind of text
	Returns a list of each word in the file.
	"""
	res = list()
	open_file = open(f)
	for line in open_file:
		for item in line.split():
			special_characters = "#$%&'()*+/<=>?@[\]^_`{|}~"
			#removing special characters using list comprehension
			word = "".join([char for char in item if char not in special_characters])
			#testing for whitespaces
			if word:
				res.append(word)
	return res
	
def count_words(t):
	"""t: word list
	This function counts each different word in given
	word list.
	"""
	res = list()
	for item in t:
		if item not in res:
			res.append(item)
	return len(res)	

def most_frequent_item(t, n=20):
	"""t: list
	n: integer. default at 20.
	This function returns the n most frequent items in t.
	"""	
	res_dict = dict()	
	for item in t:
		res_dict[item] = res_dict.get(item, 0) + 1
	
	res = list()
	for word, count in res_dict.items():
		res.append((word, count))
	
	#sorting using count as key as tuple(item, count)
	res.sort(reverse=True, key=operator.itemgetter(1))
	return res[0:n]		

def seq_difference(t1, t2):
	"""t1, t2: sequences
	Returns every item of t1 that's not in t2.
	"""	
	t1_set = set(t1)
	t2_set = set(t2)
	return list(set.difference(t1_set, t2_set))


if __name__ == "__main__":
	t1 = file_to_word_list("pg41787.txt")
	t2 = file_to_word_list("words.txt")
	print seq_difference(t1, t2)