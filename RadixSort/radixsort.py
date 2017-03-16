from random import random
from Node import Node

def makeString():
	"""
	Generate and return a random string of all printable characters from ASCII 32-126
	i.e. from chr(32) - chr(126)
	Strings are at most length 15
	"""
	s = ""
	length = random() * 15
	for i in range(int(length)):
		char = chr(int((random() * (126 - 32 + 1))) + 32)
		#don't allow first character to be a space
		if i == 0 and char == " ":
			while char == " ":
				char = chr(int((random() * (126 - 32 + 1))) + 32)
		s += char
	return s

def radix_sort(str_array, MAX_LENGTH):
	#buckets go from 0 to 126-32, 0 is the " " bucket
	#USE QUEUES
	for j in range(MAX_LENGTH, 0, -1):
		for string in str_array:
			k = MAX_LENGTH - (j - len(string)) - 1
			if k < 0:
				#categorize into the space bin
				bucket_index = 0
			else:
				#categorize into bin of string[k]
				bucket_index = ord(string[k]) - 32

class QueueLinkedList():
	"""Queue implemented as Linked List with 1 pointer:
			-- backpointer to last node. last_node.next points to
			the first node.
	"""
	def __init__(self):
		self.pointer = None

	def set_pointer(self, node):
		self.pointer = node

	def enque(self, data):
		"""Add node to front of queue.
		Return node."""
		n = Node(data)
		if self.is_empty():
			self.set_pointer(node)
			self.pointer.set_next(self.pointer)
		else:
			front = self.pointer.get_next()
			n.set_next(front)
			self.pointer.set_next(n)
			self.set_pointer(n)
		return n



	def peek(self):
		"""Returns first item in queue."""
		if self.pointer != None:
			return self.pointer.get_next()
		else:
			raise ValueError

	def deque(self):
		"""Remove node self.point points to. 
		No return value."""
		if self.is_empty() != None:
			#case: len(queue) == 1
			if self.pointer.get_next() == self.pointer:
				self.set_next(None)
			else:
				front = self.pointer.get_next()
				self.pointer.set_next(front.get_next())
				front.set_next(None)



	def is_empty(self):
		"""Return True if queue is empty, else False.
		>>> q = QueueLinkedList()
		>>> q.is_empty()
		True
		>>> n = Node(5)
		>>> q.enque(n)
		True
		>>> q.is_empty()
		False
		>>> q.deque()
		>>> q.is_empty()
		True
		"""
		return self.pointer == None








