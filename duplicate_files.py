#!/usr/bin/python

import os
import sys
import glob

def search_dir(dirname, file):
	"""dirname: file path
	file: file description
	Searches the given directory path recursively and returns a list of
	directories with files that match given file description.
	"""
	res = list()
	for root, folders, files in os.walk(dirname):
		path = glob.glob(str(os.path.join(root, file)))
		for item in path:
			res.append(item)

	#if result is empty			
	if not res:
		return "File '{}'' not found in directory '{}'.".format(file, dirname)
	else:
		return res

def duplicates(dirname, suffix):
	"""dirname: file path
	suffix: file extension
	Returns a list of files with the same file extension that are 
	essentially equal (using m5dsum) in given directory. 
	Example: duplicates(/home/, mp3)
	"""		
	file_extension = "*." + suffix
	hash_dict = dict()
	for path in search_dir(dirname, file_extension):
		cmd = "md5sum " + path
		fp = os.popen(cmd)
		hash_file = fp.read().split()
		hash_dict.setdefault(hash_file[0], []).append(hash_file[1])
	res = [files for hash, files in hash_dict.items() if len(files) > 1]
	return res
	
if __name__ == "__main__":
	for item in duplicates(*sys.argv[1:]):
		print item
	



	



