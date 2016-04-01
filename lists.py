import random
import time
import bisect

def file_words_open():
	global file_words_global
	file_words_global = open("words.txt")



def nested_sum(l):
	"""
	Receives list l, and sums all its elements, including
	nested lists. Returns: integer.
	"""
	total = 0
	for x in l:
		if type(x) != list:
			total += x
		else:
			total += sum(x)
	return total

def capitalize_all(l):
	"""
	Receives list l and for each element that is a String,
	it will return a capitalized version of it. Returns:
	new list.
	"""	
	result = []
	for s in l:
		for s in s:
			result.append(s.capitalize()) 

def cumulative_sum(l):
	"""
	Receives a list and return its cumulative sum (works
	with nested lists). Returns: new list.
	"""
	result = []
	total = 0
	for x in l:
		if type(x) == list:
			total += sum(x)
			result.append(total)
		else:
			total += x
			result.append(total)	
	return result

def middle(l):
	"""
	Receives a list and returns a new one containing all the items
	except the first and last one. Returns: new list.
	"""	
	result = []		
	for i in range(1, len(l) - 1):
		result.append(l[i])
	return result

def chop(l):
	"""
	Removes the first and last items from list l. Returns: none.
	"""		
	del l[len(l) - 1]
	del l[0]

def is_sorted(l):
	"""
	Receives list l and returns true if it is in crescent order.
	"""
	i = 0
	while i < (len(l) - 1):
		if l[i] > l[i+1]:
			return False
		i += 1	
	return True		

def is_anagram(s1, s2):
	"""
	Receives two strings and returns true if they're anagrams.
	"""	
	#Listing both strings
	s1_listed = list(s1)
	s2_listed = list(s2)

	#Capitalizing both listed strings
	s1_capitalized = capitalize_all(s1_listed)
	s2_capitalized = capitalize_all(s2_listed)

	#Sorting both listed strings
	s1_capitalized.sort()
	s2_capitalized.sort()

	if s1_capitalized == s2_capitalized:
		return True
	return False
			
def has_duplicates(l):
	"""
	Receives list l and return True if it has a duplicate item.
	"""
	for i in range(0, len(l) - 1):
		if l.count(i) > 1:
			return True
	return False		

def gen_birthday():
	"""
	Returns a list of 23 random birthdays.
	"""
	res = []
	for i in range(23):
		res.append(random.randint(1,365))
	return res
	
def bday_paradox_simulation(classes):
	"""
	Receives int class.
	Tests the probability of double birthdays appearing in classes 
	of 23 people.
	"""		
	double_bday = 0
	for i in range(classes):
		if has_duplicates(gen_birthday()) == True:
			double_bday += 1
	print "After %i simulations" %(classes),
	print "with 23 students",
	print "there were %i matches." %(double_bday),

def remove_duplicates(l):
	"""
	Receives a list and tests if it has any duplicates. If it does,
	returns a new list containing all non-duplicate items from the
	first list.
	"""
	res = []
	if has_duplicates(l) == False:
		return "There are no duplicate items in this list."
	for i in range(0, len(l) - 1):
		if l.count(l[i]) <= 1:
			res.append(l[i])
	return res	

def word_list_append():
	"""
	Returns the time it takes to append every word in words.txt to a list.
	"""
	res = []
	file_words = open("words.txt")
	start = time.time()
	for line in file_words:
		word = line.strip()
		res.append(word)
	end = time.time()
	var_time = end - start	
	print var_time

def word_list_increment():
	"""
	Returns the time it takes to increment every word in words.txt to a list.
	"""
	res = []
	file_words = open("words.txt")
	start = time.time()
	for line in file_words:
		word = line.strip()
		res += word
	end = time.time()
	var_time = end - start	
	print var_time

def word_bisect(s):
	"""
	Returns True if given word is in the words.txt file, using the bisect() function.
	"""	
	#Listing the words in words.txt
	file_words = open("words.txt")
	word_list = []
	for line in file_words:
		word = line.strip()
		word_list.append(word)
	#Searching each half of the list
	b_right = bisect.bisect_right(word_list, s)
	b_left = bisect.bisect_left(word_list, s)
	if b_right > len(word_list) - 1:
		file_words.close()
		return False
	elif b_left < 0:
		file_words.close()
		return False
	else:
		if word_list[b_right] == s or word_list[b_left] == s:
			file_words.close()
			return True
	file_words.close()
	return False

	
def reverse_pair():
	"""
	Finds all the reverse pairs in the file words.txt 
	and returns a list containing them.
	"""
	res = []
	file_words = open("words.txt")
	for line in file_words:
		word = line.strip()
		reverse_word = word[::-1]
		if word_bisect(reverse_word) == True:
			res.append(reverse_word)
			res.append(word)
			print res				
print reverse_pair()






	
		

