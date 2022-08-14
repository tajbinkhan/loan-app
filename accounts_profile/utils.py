import random
import string

def generate_string(length):
	letters = string.ascii_uppercase
	return ''.join(random.choice(letters) for i in range(length))

def generate_digit(length):
	letters = string.digits
	return ''.join(random.choice(letters) for i in range(length))