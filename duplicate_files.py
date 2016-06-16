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
	return res

	#if result is empty			
	if not res:
		return "File '{}'' not found in directory '{}'.".format(file, dirname)
	else:
		return res
	
for item in search_dir(*sys.argv[1:])	:
	print item



	



