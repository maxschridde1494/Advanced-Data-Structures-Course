from Node import Node

class LinkedBag():
	def __init__(self, head=None):
		"""if node passed into contructor, self.head = node, else self.head = None
		>>> linked = LinkedBag()
		>>> linked.get_head()
		>>> linked.get_item_count()
		0
		>>> n = Node(5)
		>>> linked2 = LinkedBag(n)
		>>> linked2.get_head().get_data()
		5
		>>> linked2.get_item_count()
		1
		"""
		if head != None:
			self.head = head
			self.itemCount = 1
		else:
			self.head = None
			self.itemCount = 0

	def get_head(self):
		"""returns head of LinkedBag
		"""
		return self.head

	def get_item_count(self):
		return self.itemCount

	def increment_count(self):
		self.itemCount += 1

	def set_head(self, node):
		self.head = node

	def is_empty(self):
		"""returns True if LinkedBag is empty, False otherwise.
		"""
		return self.itemCount == 0

	def getCurrentSize(self):
		"""returns number if items in LinkedBag
		"""
		return self.itemCount

	def initialize_from_vector(self, vector):
		"""if empty, initialize LinkedBag from vector and return True. Otherwise, return false
		>>> lb = LinkedBag()
		>>> lb.initialize_from_vector([])
		False
		>>> lb.initialize_from_vector([1])
		True
		>>> lb.vector()
		[1]
		>>> lb.get_item_count()
		1
		>>> lb2 = LinkedBag()
		>>> lb2.initialize_from_vector([1,2,3])
		True
		>>> lb2.vector()
		[1, 2, 3]
		>>> lb2.get_item_count()
		3
		>>> lb2.initialize_from_vector([4,5,6])
		False
		>>> lb2.vector()
		[1, 2, 3]

		"""
		if self.is_empty() and len(vector) > 0:
			n = Node(vector[0])
			front = n
			self.increment_count()
			if len(vector) > 1:
				for index in range(1, len(vector)):
					temp = Node(vector[index])
					n.set_next(temp)
					n = temp
					self.increment_count()
			self.set_head(front)
			return True
		return False

	def vector(self):
		"""Returns contents of LinkedBag as vector
		>>> lb = LinkedBag()
		>>> lb.vector()
		[]
		>>> lb = LinkedBag()
		>>> n = Node(1)
		>>> n2 = Node(2)
		>>> n3 = Node(3)
		>>> n.set_next(n2)
		>>> n2.set_next(n3)
		>>> lb.set_head(n)
		>>> lb.vector()
		[1, 2, 3]

		"""
		l = []
		curr = self.get_head()
		while curr != None:
			l.append(curr.get_data())
			curr = curr.get_next()
		return l

	def add(self, data):
		"""
		if data == None, returns False.
		else, make new node, add node to front of LinkedBag, increment itemCount, and return True.
		>>> lb = LinkedBag()
		>>> lb.add('hello')
		True
		>>> lb.vector()
		['hello']
		>>> lb.get_item_count()
		1
		>>> lb.add(1)
		True
		>>> lb.vector()
		[1, 'hello']
		>>> lb.get_item_count()
		2
		>>> lb2 = LinkedBag()
		>>> lb2.initialize_from_vector([1,2,3])
		True
		>>> lb2.add(None)
		False
		>>> lb2.add(5)
		True
		>>> lb2.get_item_count()
		4
		>>> lb2.vector()
		[5, 1, 2, 3]
		"""
		if data != None:
			node = Node(data)
			node.set_next(self.head)
			self.head = node
			self.itemCount += 1
			return True
		return False

	def contains(self, data):
		"""
		returns True if bag contains data, or false otherwise
		>>> lb = LinkedBag()
		>>> lb.contains(2)
		False
		>>> lb.initialize_from_vector([1,2,3])
		True
		>>> lb.contains(5)
		False
		>>> lb.contains(1)
		True
		>>> lb.contains(3)
		True
		>>> lb.add('hello')
		True
		>>> lb.contains('hello')
		True
		"""
		curr = self.head
		while curr != None:
			if curr.get_data() == data:
				return True
			curr = curr.get_next()
		return False


	def remove(self, data):
		"""if node with data is in LinkedBag, remove ONE/FIRST OCCURRENCE, decrement itemCount and return True.
		Otherwise, return False
		>>> lb = LinkedBag()
		>>> lb.initialize_from_vector([1,3,2,3,3])
		True
		>>> lb.remove(3)
		True
		>>> lb.vector()
		[1, 2, 3, 3]
		>>> lb.contains(3)
		True
		>>> lb.remove(1)
		True
		>>> lb.vector()
		[2, 3, 3]
		>>> lb.remove(2)
		True
		>>> lb.remove('hello')
		False
		>>> lb.remove(3)
		True
		>>> lb.remove(3)
		True
		>>> lb.remove(3)
		False
		"""
		if self.contains(data):
			#self.head contains data
			if self.get_head().get_data() == data:
				self.set_head(self.get_head().get_next())
				removed = True
			else:
				curr_node = self.head
				next_node = curr_node.get_next()
				removed = False
				while not removed:
					if next_node.get_data() == data:
						curr_node.set_next(next_node.get_next())
						removed = True
					else:
						curr_node = next_node
						next_node = next_node.get_next()
			self.itemCount -= 1
			return removed
		return False
