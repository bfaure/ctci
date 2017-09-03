'''
Write a function to return the kth to last element of a singly linked list
'''

from linked_list import linked_list

# returns the kth to last element in the linked list
def kth_element(a_list,index):
	true_idx = a_list.length()-index
	return a_list[true_idx]

# inserts 'count' random integers to the provided list
def add_rand_elements(a_list,count=200):
	from random import randint
	for _ in range(count):
		a_list.append(randint(0,100))
	return a_list

my_list = linked_list()
my_list = add_rand_elements(my_list)

print kth_element(my_list,1)
