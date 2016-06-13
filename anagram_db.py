import anydbm
import anagram
import pickle

def dict_to_db(t):
	"""
	t: dictionary
	Converts given dictionary to a db file.
	"""
	db = anydbm.open("dict_to_db.db", "c")
	for key, val in t.items():
		db[key] = pickle.dumps(val)

def read_db(db):
	"""db: database file created using dict_to_db() function
	Reads given database file and prints keys and values to screen.
	"""
	open_db = anydbm.open(db, "r")
	for key, val in open_db.items():
		print key, pickle.loads(val)

def read_key(key, db):
	"""key: string
	db: database file
	Prints value(s) of given key in db file.
	"""		
	open_db = anydbm.open(db, "r")
	print pickle.loads(open_db[key])

def read_anagrams(word, db):
	"""word: string
	db: database file
	Prints a list of anagrams of given word.
	"""	
	open_db = anydbm.open(db, "r")
	res = open_db["".join(sorted(word))]

	print "Anagrams of {word}:".format(word=word)
	for item in pickle.loads(res):
		if item != word:
			print "-", item	

if __name__ == "__main__":
	test_dictionary = anagram.anagram("words.txt")
	dict_to_db(test_dictionary)
	read_anagrams("traced", "dict_to_db.db")





