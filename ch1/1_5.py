'''
There are three types of operations that can be performed
on a string: insert a char, remove a char, or replace a char.
Write a function, that, provided two strings, checks if they
are 1 (or zero) operations away from being identical.
'''

# checks if inputs are 1 or zero operations away
# from being identical
def check_num_operations(str1,str2):
	if str1==str2:
		print "0 operations"
		return 0
	if abs(len(str1)-len(str2))>1:
		print ">1 operations"
		return -1
	
	# if the strings are the same length
	if len(str1)==len(str2):
		# record number of char differences
		num_diff = 0
		for s1,s2 in zip(str1,str2):
			if s1!=s2: num_diff+=1
		if num_diff==1:
			print "1 operation"
			return 1
		else:
			print ">1 operations"
			return -1

	# if the first string is shorter
	if len(str1)<len(str2):
		# check if the beginning of the longer string equals the shorter
		if str1==str2[:-1]:
			print "1 operation"
			return 1
		else:
			print ">1 operations"
			return -1
	# if the second string is shorter
	if len(str2)<len(str1):
		if str2==str1[1:]:
			print "1 operation"
			return 1
		else:
			print ">1 operations"
			return -1

str1 = "th"
str2 = "the"

check_num_operations(str1,str2)