import os

def walk(dirname):
	"""dirname: directory
	Lists all folders and files in given directory.
	"""
	for dirpath, dirname, filename in os.walk(dirname):
		for name in filename:
			print os.path.join(dirpath, name)
		for name in dirname:
			print os.path.join(dirpath, name)	

walk(os.getcwd())