import os

def search_dir(dirname, file):
	"""dirname: file path
	file: file description
	Searches the given directory path recursively and returns a list of
	directories with files that match given file description.
	"""
	
	res = list()

	for root, folders, files in os.walk(dirname):
		for name in files:
			if name == file:
				res.append((os.path.join(root, name)))
	
	#if result is empty			
	if not res:
		return "File '{}'' not found in directory '{}'.".format(file, dirname)
	else:
		return res

	



