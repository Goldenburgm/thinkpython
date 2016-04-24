from fractions import gcd

p = 17
q = 41
n = p * q
totient = (p-1) * (q-1)
public_key1 = 13 #this is e
public_key2 = n

def is_prime(n):
	"""n: positive integer
	Returns true if given number is a prime.
	"""
	#Testing for 0 and 1
	if n < 2:
		return False
	#Tests for pairs	
	if n % 2 == 0:
		return n == 2
	div = 3
	#Testing the power of every 
	#odd number smaller than n
	while div * div <= n:
		if n % div == 0:
			return False
		div += 2
	return True

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

def encrypt_message(m):
	"""m: message encoded by encode_message() function
	Encrypts a message using the RSA method.
	"""	
	res = []
	for item in m:
		encrypted_char = item ** public_key1 % public_key2
		res.append(encrypted_char)
	return res	

def extended_euclides(a, b):
	"""
	a, b: integers
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
	"""
	a, b: integers
	Returns the modular inverse of a and b, using the euclidean
	extended algorithm.
	"""
	#this function will receive the totient
	#and public_key1, to find the private
	#key
	g, x, y = extended_euclides(a, b)
	if g != 1:
		return None
	else:
		return x % b

def decrypt_message(m, private_key):
	"""Receives: message encrypted by encrypt_message() function
	and private key.
	Returns decrypted message.
	"""
	res = []
	for item in m:
		decrypted = chr(item ** private_key % n)
		res.append(decrypted)
	return res

coded_message = encode_message("this is a message")	
encrypted_message = encrypt_message(coded_message)

print coded_message
print encrypted_message
print mod_inverse(public_key1, totient)
print decrypt_message(encrypted_message, mod_inverse(public_key1, totient))


