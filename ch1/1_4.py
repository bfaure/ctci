'''
Given a string, write a function to check if it's a 
permutation of a palindrome. A palindrom is a word or
phrase that is the same backwards and forwards.
'''

# function to check if string is palindrome
def is_palindrome(string):
	idx0 = 0
	idx1 = len(string)-1

	while True:
		if string[idx0]!=string[idx1]:
			print "Not a palindrome"
			return False
		idx0+= 1
		idx1+=-1
		if idx0>=idx1: break
	print "Palindrome"
	return True

# function to check if a permutation is a palindrome
def is_permutation_palindrome(string):
	# going to check if each character has an even number of instances
	seen_chars=[]
	seen_chars_cts=[]

	# get character counts
	for char in string:
		if char in seen_chars:
			seen_chars_cts[seen_chars.index(char)]+=1
		else:
			seen_chars.append(char)
			seen_chars_cts.append(1)

	# check number of odd instances
	num_odd=0
	for ct in seen_chars_cts:
		if ct % 2 != 0: num_odd+=1

	# evaluate whether or not permutation could be palindrome
	if num_odd<=1:
		print "Permutation is a palindrome"
		return True
	else:
		print "No palindromes"
		return False

is_permutation_palindrome("racecar")