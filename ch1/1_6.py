'''
Implement a function to perform a basic string compression.
For example, provided the string 'aabbcc' you would return
'a2b2c2'. If the compressed string would not be shorter than
the original string, you should return the original. Assume
only uppercase and lowercase letters.
'''

def compress(string):
	compressed 	= ''
	last_char 	= None
	count 		= 0

	for char in string:
		if last_char==None:
			last_char = char 
			count 	  = 1
		else:
			if char==last_char:
				count+=1
			else:
				compressed += "%s%d" % (last_char,count)
				last_char 	= char 
				count 		= 1

	if last_char!=None:
		compressed += "%s%d" % (last_char,count)

	if len(compressed)<len(string):
		print "Compressed to: %s" % compressed 
		return compressed 
	else:
		print "Not compressed"
		return string


compress("aabbccc")

