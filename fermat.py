import math

a = int(raw_input("Type a value a:\n"))
b = int(raw_input("Type a value b:\n"))
c = int(raw_input("Type a value c:\n"))
n = int(raw_input("Type a value n:\n"))


def check_fermat():
	if (math.pow(a, n) + math.pow(b, n) == math.pow(c, n)) and (n > 2):
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work."

check_fermat()

