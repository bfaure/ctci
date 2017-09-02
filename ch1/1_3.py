'''
Given a string, write a function that replaces all spaces
with the string '%20'. Try to implement in-place.
'''

# not in-place version
def urlify(string):
	new_str = ""
	for char in string:
		if char!='': new_str+=char
		else: 		 new_str+='%20'
	return new_str
