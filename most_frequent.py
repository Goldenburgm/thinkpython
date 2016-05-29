def file_list(file_arg):
	"""Receives a file and converts it into a list. List has global access.
	"""	
	global file_list_var
	file_list_var = []
	open_file = open(file_arg)
	for line in open_file:
		item = line.strip()
		file_list_var.append(item)

def most_frequent(word):
	"""word: string
	Counts characters in given string and yields the frequency
	of each character.
	"""
	t = []
	for char in word:
		freq = word.count(char)
		t.append((freq, char))
	
	#removing repeated items	
	t = list(set(t))

	#yielding each char in list t
	for freq, char in t:
		yield char, freq

file_list("words.txt")

res = dict()

#first we sum the char frequency in a dict
for word in file_list_var:
	for char, freq in most_frequent(word):
		res[char] = res.get(char, 0) + 1

res_list = list()		

#then we convert it to a list and sort it
for char, freq in res.items():
	res_list.append((freq, char))
	res_list.sort(reverse=True)

for freq, char in res_list:
	print freq, char






	