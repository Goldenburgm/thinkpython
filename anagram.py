def anagram(f):
	"""f: word file (one word per line)
	Reads given file and prints a list containing all anagrams in file,
	in descending order.
	"""
	open_file = open(f)
	anagrams_dict = dict()
	
	for line in open_file:
		word = line.strip()
		#sorting each word
		sorted_word = "".join(sorted(word))
		#using setdefault to initialize sorted_word 
		#key with an empty list
		anagrams_dict.setdefault(sorted_word, []).append(word)
	
	#anagrams = list()

	#searching for every value greater than one in dict
	#value = number of items in list of words
	#for key, value in anagrams_dict.items():
	#	if len(value) > 1:
	#		anagrams.append(value)

	#sorting anagram list by length, in decreasing order
	#anagrams.sort(key=len, reverse=True)

	#for item in anagrams:
	#	print item, len(item)

	return anagrams_dict


if __name__ == "__main__":	
	print anagram("words.txt")		