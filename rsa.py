import random
import math

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
	prime_list = []
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
	return public_key1, public_key2, private_key

def encrypt_message(m, public_key1, public_key2):
	"""m: message encoded by encode_message() function
	Encrypts a message using the RSA method.
	"""	
	res = []
	for item in m:
		encrypted_char = ord(item) ** public_key1 % public_key2
		res.append(encrypted_char)
	return res	

def decrypt_message(m, private_key):
	"""m: message encrypted by encrypt_message() function
	private_key: integer returned by mod_inverse()
	Returns decrypted message.
	"""
	res = []
	for item in m:
		decrypted = chr((item ** private_key % public_key2))
		res.append(decrypted)
	return res

keys = keypair_gen()
public_key1 = keys[0]
public_key2 = keys[1]
private_key = keys[2]

print public_key1
print public_key2
print private_key
print keys

encrypted = encrypt_message("abc", keys[0], keys[1])
print decrypt_message(encrypted, keys[2])
