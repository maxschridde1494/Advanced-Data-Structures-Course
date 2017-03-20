class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		"""
		>>> n = Node()
		>>> n.get_data()
		>>> n1 = Node(1)
		>>> n1.get_data()
		1
		"""
		return self.data

	def get_next(self):
		"""
		>>> n = Node()
		>>> n.get_next()
		>>> n1 = Node(1)
		>>> n1.get_next()
		>>> n2 = Node(5, n1)
		>>> n2.get_next().get_data()
		1
		"""
		return self.next_node

	def set_next(self, new_next):
		"""
		>>> n1 = Node(1)
		>>> n1.get_next()
		>>> n2 = Node(5)
		>>> n1.set_next(n2)
		>>> n1.get_next().get_data()
		5
		"""
		self.next_node = new_next