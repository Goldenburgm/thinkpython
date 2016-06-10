import string as s
import operator as op
import matplotlib.pyplot as pyplot
import sys

def file_word_frequency(f):
	"""f: file
	Returns a list where each item is composed of a word and
	the frequency of that word in given file. Ignores punctuation and
	uppercase.
	"""
	t = dict()
	open_file = open(str(f))
	for line in open_file:
		for item in line.split():
			#removing punctuation
			word = "".join([char.lower() for char in item if 
							char not in s.punctuation])
			t[word] = t.get(word, 0) + 1
	res = [(word, freq) for (word, freq) in t.items()]
	#sorting in reverse order by the frequency in each item	
	res.sort(reverse=True, key=op.itemgetter(1))
	return res

def main(name, file_name="pg41787.txt", flag="plot"):
	"""file_name = name of file to plot or print results
	flag = plot or print
	Depending on flag, prints or plots the frequency of words in given
	file, in descending order.
	"""
	#using enumerate to make a list containing (rank, frequency)
	zipfs_list = [(item[1], rank) for rank, item in 
				  enumerate(file_word_frequency(file_name))]
	
	ranks, frequencies = zip(*zipfs_list)

	if flag == "plot":
		pyplot.plot(ranks, frequencies, "r-")
		pyplot.ylabel("Frequency")
		pyplot.xlabel("Rank")
		pyplot.show()
	elif flag == "print":
		for frequency, rank in zipfs_list:
			print rank, frequency
	else:
		print "Usage: ./zipfs.py filename [print|plot]"		
	
if __name__ == "__main__":
	main(*sys.argv)