
import sys

class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None

class binary_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None: self.root=node(value)
		else: 			    self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child!=None: self._insert(value,cur_node.left_child)
			else: 						  cur_node.left_child=node(value)
		else:
			if cur_node.right_child!=None: self._insert(value,cur_node.right_child)
			else: 						   cur_node.right_child=node(value)

	def find(self,value):
		return self._find(value,self.root) if self.root!=None else None

	def _find(self,value,cur_node):
		if value==cur_node.value: 
			return cur_node 
		elif value<cur_node.value and cur_node.left_child!=None: 
			self._find(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			self._find(value,cur_node.right_child)

	def print_tree(self):
		if self.root!=None: self._print_tree(self.root)

	def _print_tree(self,cur_node):
		if cur_node!=None:
			self._print_tree(cur_node.left_child)
			print "%d "%cur_node.value
			self._print_tree(cur_node.right_child)

	def depth(self):
		return self._depth(self.root,0) if self.root!=None else 0

	def _depth(self,cur_node,cur_depth):
		if cur_node==None: return cur_depth
		left_depth=self._depth(cur_node.left_child,cur_depth+1)
		right_depth=self._depth(cur_node.right_child,cur_depth+1)
		return max(left_depth,right_depth)

	def display(self):
		levels=[]
		cur_nodes=[self.root]
		while True:
			if len(cur_nodes)==0: break
			cur_values=[]
			next_nodes=[]
			for n in cur_nodes:
				if n.value!=None:       cur_values.append(n.value)
				if n.left_child!=None:  next_nodes.append(n.left_child)
				if n.right_child!=None: next_nodes.append(n.right_child)
			levels.append(cur_values)
			cur_nodes=next_nodes
		for i,level in enumerate(levels):
			sys.stdout.write("Level %d:  "%i)
			for n in level:
				sys.stdout.write("%d "%n)
			sys.stdout.write("\n")

tree = binary_tree()
tree.insert(3)
tree.insert(4)
tree.insert(0)
tree.insert(8)
tree.insert(2)

tree.print_tree()

tree.display()



