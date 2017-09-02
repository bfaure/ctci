'''
Create function that detects if either of the two input
strings is a permutation of the other.
'''

def is_permutation(str1,str2):
	if len(str1)!=len(str2):
		print "Not permuatation!"
		return False

	str1 = ''.join(sorted(str1))
	str2 = ''.join(sorted(str2))

	if str1!=str2:
		print "Not permutation!"
		return False
	print "Permutation!"
	return True

str1 = "cba"
str2 = "abc"

is_permutation(str1,str2)