from Node import Node

class QueueLinkedList():
	"""Queue implemented as Linked List with 1 pointer:
			-- backpointer to last node. last_node.next points to
			the first node.
	"""
	def __init__(self):
		self.pointer = None

	def set_pointer(self, node):
		self.pointer = node

	def get_pointer(self):
		return self.pointer

	def enque(self, data):
		"""Add node to front of queue.
		Return True if enqueues, False otherwise.
		>>> q = QueueLinkedList()
		>>> q.enque(5)
		True
		>>> q.peek().get_data()
		5
		>>> q.enque(None)
		False
		>>> q.enque(3)
		True
		>>> q.get_pointer().get_data()
		3
		"""
		if data != None:
			n = Node(data)
			if self.is_empty():
				self.set_pointer(n)
				self.pointer.set_next(self.pointer)
			else:
				front = self.pointer.get_next()
				n.set_next(front)
				self.pointer.set_next(n)
				self.set_pointer(n)
			return True
		return False



	def peek(self):
		"""Returns first item in queue.
		>>> q = QueueLinkedList()
		>>> q.enque(5)
		True
		>>> q.peek().get_data()
		5
		>>> q.enque(None)
		False
		>>> q.peek().get_data()
		5
		>>> q.enque(3)
		True
		>>> q.enque(4)
		True
		>>> q.get_pointer().get_data()
		4
		"""
		if self.pointer != None:
			return self.pointer.get_next()
		else:
			raise ValueError

	def deque(self):
		"""Remove node self.point points to. 
		No return value.
		>>> q = QueueLinkedList()
		>>> q.deque()
		>>> q.is_empty()
		True
		>>> q.enque(5)
		True
		>>> q.deque()
		>>> q.is_empty()
		True
		>>> q.enque(5)
		True
		>>> q.enque(4)
		True
		>>> q.enque(3)
		True
		>>> q.deque()
		>>> q.peek().get_data()
		4
		>>> q.get_pointer().get_data()
		3
		>>> q.deque()
		>>> q.peek().get_data()
		3
		>>> q.deque()
		>>> q.is_empty()
		True
		"""
		if self.is_empty() != True:
			#case: len(queue) == 1
			if self.pointer.get_next() == self.pointer:
				self.set_pointer(None)
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








