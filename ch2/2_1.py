'''
Write code to remove duplicates from a unsorted linked list
'''

from linked_list import linked_list

# inserts 'count' random integers to the provided list
def add_rand_elements(a_list,count=200):
	from random import randint
	for _ in range(count):
		a_list.append(randint(0,100))
	return a_list

# removes any duplicates found in the linked list
def remove_duplicates(a_list):
	seen=[]
	list_length=a_list.length()
	cur_idx=0
	while True:
		cur=a_list[cur_idx]
		if cur in seen:
			a_list.erase(cur_idx)
			list_length+=-1
		else:
			seen.append(cur)
		cur_idx+=1
		if cur_idx>=list_length:
			break

'''
to perform remove_duplicates w/o a temporary buffer (seen), you
can re-write remove_duplicates with a second loop, iterate over
each elem in first loop, in inner, compare current with outer loop 
value and delete if the same
'''

my_list = linked_list()
my_list = add_rand_elements(my_list)
print my_list.length()

remove_duplicates(my_list)
print my_list.length()