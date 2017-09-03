'''
Write a function to delete a middle node of a singly linked list. The
function parameter is the node you wish to delete, not the linked_list
itself.
'''

from linked_list import linked_list

# deletes the passed node in the overall linked list
def delete_node(node):
	return node.next 

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

head = my_list.head
first = head.next # 1
second = first.next # 2
third = second.next # 3
fourth = third.next # 4

my_list.display()
second = delete_node(second)
my_list.display()



