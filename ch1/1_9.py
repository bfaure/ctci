'''
Assume you are provided a function called is_substring which checks
if it's first argument is a substring of the second. Write code to
check if a string is a rotation of another string using this function.
For example; "erbottlewat" is a rotation of "waterbottle"
'''

# first, writing the is_substring function
def is_substring(str1,str2):
	return str1 in str2


# function to check if the first string is a rotation of the second,
# using the is_substring function
def is_rotation(str1,str2):
	concat = str1+str1
	return is_substring(str2,concat)

str1 = "erbottlewat"
str2 = "waterbottle"
print is_rotation(str1,str2)