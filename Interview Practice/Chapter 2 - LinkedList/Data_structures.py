#!/usr/bin/python3
# This is just an implementatinon of all basic data structures, 
# built from scratch using Nodes/LinkedList for learning purposes

class Node:
	"""
	Generic Node Class | Can be doubly or singly
	"""
	def __init__(self, data=None):
		"""
			Type argument changes behavior to singly, or doubly
		"""
		if data:
			self.val = data
		else:
			self.val = None
		self.next = None
		self.prev = None

	def appendToTail(self, data, typeChar='d'):
		"""
		O(n), will need to traverse and place at end
		typeChar default is d, explictly use s for singly
		"""
		newNode = Node(data)
		pointer = self
		while(pointer.next != None):
			pointer = pointer.next
		pointer.next = newNode
		if typeChar == 'd':
			newNode.prev = pointer
			
	def printLinkedList(self):
		"""
		Helper Method to print out the linkedList
		"""
		pointer = self
		# Cause I want to not put the - after last element
		while(pointer.next != None):
			print(str(pointer.val) + ' - ',end='')
			pointer = pointer.next
		print(str(pointer.val))

	def findNode(self, value):
		"""
			Helper Node to find Node given Value. 
			Will return Node reference of Node given a payload value
			else, it will return None
		"""
		pointer = self
		while(pointer != None):
			if pointer.val == value:
				return pointer
			pointer = pointer.next
		return None

class Stack:
	"""
		LIFO || push, peek, pop, and isEmpty. 
		Value is any payload. 
		Needs node class
	"""
	def __init__(self):
		self.head = Node(None)
		self.size = 0

	def push(self, data):
		if self.isEmpty():
			self.head.val = data
		else:
			self.head.next = Node(data)
			self.head.next.prev = self.head
			self.head = self.head.next
		self.size += 1

	def peek(self):
		if self.isEmpty():
			raise ValueError('Stack has no elements')
		else:
			return self.head.val

	def pop(self):
		if self.isEmpty():
			raise ValueError('Stack has no elements')
		elif self.size == 1:
			result = self.head.val
			self.head.val = None
			self.size -= 1
			return result
		else:
			result = self.head.val
			self.head = self.head.prev
			self.head.next = None
			self.size -= 1
			return result

	def isEmpty(self):
		return self.size == 0

class Queue:
	"""
		FIFO || implements add, remove, examine, and isEmpty
	"""
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def isEmpty(self):
		return self.size == 0

	def add(self, value):
		newNode = Node(value)
		if self.isEmpty():
			self.head = newNode
			self.tail = newNode
		else:
			self.head.next = newNode
			self.head.next.prev = self.head
			self.head = newNode
		self.size += 1

	def remove(self):
		if self.isEmpty():
			raise ValueError('Queue has no elements')
		elif self.size == 1:
			result = self.tail.val
			self.head = None
			self.tail = None
			self.size -= 1
			return result
		else:
			result = self.tail.val
			self.tail = self.tail.next
			self.tail.prev = None
			self.size -= 1
			return result

	def examine(self):
		if self.isEmpty():
			raise ValueError('Queue has no elements')
		else:
			return self.tail.val

class TreeNode:
	"""
		Binary Tree Node, not Full/Complete/Balanced
	"""
	def __init__(self, data=None):
		if data:
			self.val = data
		else:
			self.val = None
		self.left = None
		self.right = None

	def inOrderPrint(self, root):
		if root != None:
			self.inOrderPrint(root.left)
			print(root.val)
			self.inOrderPrint(root.right)
		return
	
	def preOrderPrint(self, root):
		if root != None:
			print(root.val)
			self.preOrderPrint(root.left)
			self.preOrderPrint(root.right)
		return
	
	def postOrderPrint(self, root):
		if root != None:
			self.postOrderPrint(root.left)
			self.preOrderPrint(root.right)
			print(root.val)
		return

def main():
	# 1 will test queue, 2 will test Tree
	test = 2
	if test == 1:
		# Queue Test
		myQueue = Queue()
		myQueue.add(50)
		myQueue.add('Test')
		myQueue.add(50)
		print(myQueue.remove())
		print(myQueue.examine())
		print(myQueue.remove())
		print(myQueue.examine())
		print(myQueue.remove())
	if test == 2:
		# Visual Representation
		#
		#			50
		#		/ 		 \
		#     30		  70
		#    /  \        
		#  10   40
		root = TreeNode(50)
		root.left = TreeNode(30)
		root.right  = TreeNode(70)
		root.left.left = TreeNode(10)
		root.left.right = TreeNode(40)
		root.postOrderPrint(root)

if __name__ in '__main__': main()