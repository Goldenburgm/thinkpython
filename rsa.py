import random
import math
import collections
import os

def is_prime(n):
	"""n: positive integer
	Returns True if given number is a prime, using Fermat's Little Theorem.
	"""
	if n == 2:
		return True
	if not n and 1:
		return False
	return pow(2, n-1, n) == 1		

def random_prime():
	"""Returns a random prime number.
	"""	
	notPrime = True
	while notPrime == True:
		n = random.getrandbits(8)
		if is_prime(n) == True:
			notPrime = False
	return n		

def random_prime_range(a, b):
	"""a, b: positive integers
	Returns a random prime between a and b.
	"""	
	notPrime = True
	while notPrime == True:
		n = random.randrange(a, b)
		if is_prime(n):
			notPrime = False
	return n		
		
def encode_message(m):
	"""m: string
	Receives message m and converts it to integers, using the ord()
	function. Returns a new list with the encoded message.
	"""	
	res = []
	message_list = list(m)
	for item in message_list:
		encoded_char = ord(item)
		res.append(encoded_char)	
	return res

def extended_euclides(a, b):
	"""a, b: integers
	Precondition: at least one of the integers must be greater
	than zero.
	Returns the result of the extended Euclides algorithm.
	"""
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = extended_euclides(b % a, a)
		return (g, x - (b // a) * y, y)

def mod_inverse(a, b):
	"""a, b: integers
	Returns the modular inverse of a and b, using the euclidean
	extended algorithm. Used in the RSA method to find the 
	private key.
	"""
	#this function will receive the totient
	#and public_key1, to find the private
	#key
	g, x, y = extended_euclides(a, b)
	if g != 1:
		return None
	else:
		return x % b		

def keypair_gen():
	"""Generates a pair of public keys and a private key using
	the RSA method.
	"""
	p = random_prime()
	q = random_prime()
	totient = (p-1) * (q-1)
	public_key1 = random_prime_range(1, totient) #this is e
	public_key2 = p * q #this is n
	private_key	= mod_inverse(public_key1, totient)
	return public_key1, public_key2, private_key, totient

def encrypt_message(m, public_key1, public_key2):
	"""m: message encoded by encode_message() function
	Encrypts a message using the RSA method.
	"""	
	res = []
	for item in m:
		#converting each char to an int using ord()
		encrypted_char = ord(item) ** public_key1 % public_key2
		res.append(encrypted_char)
	return res	

def decrypt_message(m, private_key, public_key2):
	"""m: message encrypted by encrypt_message() function
	private_key: integer returned by mod_inverse()
	Returns decrypted message.
	"""
	res = []
	for item in m:
		#converting every int back to a char using chr()
		decrypted = chr(int(item) ** private_key % public_key2)
		res.append(decrypted)
	return res

def save_to_file(content, file_name):
	"""content: any data type
	file_name: String. 
	Create file named file_name containing whatever was issued to the
	parameter content. This function assumes the file is a txt. The resulting file contains
	"""
	new_file = open(file_name, 'w')
	#if the content is iterable
	if isinstance(content, collections.Iterable): 
		for item in content:
			new_file.write(str(item)) 
			new_file.write("\n")
	else:
		#converting content to str to avoid character buffer exception	
		new_file.write(str(content)) 

def file_to_list(file_name):
	"""Receives file and returns a list contaning one item per line of the
	file.
	"""	
	open_file = open(file_name)
	res = []
	for line in open_file:
		item = line.strip()
		res.append(item)	
	return res	

def a_choice():
	"""
	"""
	notChosen = True
	while notChosen == True:
		print "Choose an option:"
		print "A - Generate public and private key"
		print "B - Encrypt message (requires public key)"
		print "C - Decrypt message (requires private key)"
		print "D - Exit script"
		choice = raw_input("> ")

		if str(choice.upper()) == "A":
			print "Generating your keys..."
			keys = keypair_gen()
			public_key1 = keys[0]
			public_key2 = keys[1]
			private_key = keys[2]
			save_to_file(public_key1, "pub_key1.txt")
			save_to_file(public_key2, "pub_key2.txt")
			save_to_file(private_key, "priv_key.txt")

		elif str(choice.upper()) == "B":	
			print "Type the message you wish to encrypt: "
			message = raw_input("> ")
			print "Using the public keys in your current directory"
			print "to encrypt your message..."
			pub_key1_file = open("pub_key1.txt")
			pub_key2_file = open("pub_key2.txt")
			#read each pub_key file as an int
			pub_key1 = int(pub_key1_file.read()) 
			pub_key2 = int(pub_key2_file.read())
			encrypted_message = encrypt_message(message, pub_key1, pub_key2)
			save_to_file(encrypted_message, "encrypted_message.txt")
			print "Your message is in the encrypted_message.txt file."

		elif str(choice.upper()) == "C":
			print "Searching for a encrypted message and private key"
			print "in your current directory..."
			pub_key2_file = open("pub_key2.txt")
			priv_key_file = open("priv_key.txt")
			pub_key2 = int(pub_key2_file.read())
			priv_key = int(priv_key_file.read())
			message = file_to_list("encrypted_message.txt")
			decrypted_message = decrypt_message(message, priv_key, pub_key2)
			#joining list to a readable string
			decrypted_message_string = "".join(decrypted_message)
			print decrypted_message_string

		elif str(choice.upper()) == "D":
			notChosen = False


a_choice()







