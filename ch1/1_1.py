
'''
Create function to check if all characters in a string
are unique. What if you cannot use additional data structures.
'''

# Using extra list data structure
def unique_char_checker(string):
	seen = []
	for char in string:
		if char in seen:
			print "Not Unique"
			return False
		else:
			seen.append(char)
	print "Unique"
	return True

# Not using additional data structure
def unique_char_checker2(string):
	for i in range(len(string)):
		for j in range(i+1,len(string)):
			if string[i]==string[j]:
				print "Not unique"
				return False
	print "Unique"
	return True

unique_char_checker("aslkd;fjaslk;d")
unique_char_checker2("abcdefg")