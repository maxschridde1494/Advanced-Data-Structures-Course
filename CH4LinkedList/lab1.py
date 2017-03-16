from LinkedBag import LinkedBag

class Set():
	def __init__(self, linkedbag=LinkedBag()):
		if linkedbag.get_head() != None:
			#make LinkedBag contain unique items
			lb = LinkedBag()
			lb.initialize_from_vector(list(set(linkedbag.vector())))
			linkedbag = lb
		self.lb = linkedbag

	def get_linked_bag(self):
		return self.lb

	def set_linked_bag(self, linkedbag):
		self.lb = linkedbag

	def getCurrentSize(self):
		return self.lb.getCurrentSize()

	def isEmpty(self):
		return self.lb.is_empty()

	def add(self, data):
		"""Add element to Set if not already in LinkedBag. Return True if added, False otherwise.
		>>> lb1 = LinkedBag()
		>>> lb1.initialize_from_vector([1,2,3])
		True
		>>> s1 = Set(lb1)
		>>> s2 = Set()
		>>> s1.add(3)
		False
		>>> s1.add(5)
		True
		>>> s1.getCurrentSize()
		4
		>>> s1.get_linked_bag().vector()
		[5, 1, 2, 3]
		>>> s2.get_linked_bag().vector()
		[]
		"""
		if not self.lb.contains(data):
			return self.lb.add(data)
		else:
			return False

	def remove(self, data):
		return self.lb.remove(data)

	def __add__(self, set2):
		"""Return a new Set which is the union of self and the passed in set2
		>>> lb1 = LinkedBag()
		>>> lb1.initialize_from_vector([1,2,3])
		True
		>>> s1 = Set(lb1)
		>>> lb2 = LinkedBag()
		>>> lb2.initialize_from_vector([3,4,5])
		True
		>>> s2 = Set(lb2)
		>>> s3 = s1 + s2
		>>> s3.get_linked_bag().vector()
		[1, 2, 3, 4, 5]
		>>> s4 = s2 + s1
		>>> s4.get_linked_bag().vector()
		[1, 2, 3, 4, 5]
		>>> s5 = Set()
		>>> s6 = Set()
		>>> s7 = s5 + s6
		>>> s7.get_linked_bag().vector()
		[]
		"""

		#PYTHONIC WAY
		# self_vec = self.lb.vector()
		# lb2_vec = set2.get_linked_bag().vector()
		# lb_new = LinkedBag()
		# lb_new.initialize_from_vector(list(set(self_vec) | set(lb2_vec)))
		#return Set(lb_new)

		#Iterate through LinkedBag without using Python shortcuts
		lb = LinkedBag()
		self_vec = self.lb.vector()
		curr = set2.get_linked_bag().get_head()
		while curr != None:
			if not self.lb.contains(curr.get_data()):
				self_vec.append(curr.get_data())
			curr = curr.get_next()
		lb.initialize_from_vector(self_vec)
		return Set(lb)

	def __sub__(self, set2):
		"""Return a new Set which is the intersection of self and the passed in set2
		>>> lb1 = LinkedBag()
		>>> lb1.initialize_from_vector([1,2,3])
		True
		>>> s1 = Set(lb1)
		>>> lb2 = LinkedBag()
		>>> lb2.initialize_from_vector([3,4,5])
		True
		>>> s2 = Set(lb2)
		>>> s3 = s1 - s2
		>>> s3.get_linked_bag().vector()
		[3]
		>>> s4 = s2 - s1
		>>> s4.get_linked_bag().vector()
		[3]
		>>> s5 = Set()
		>>> s6 = Set()
		>>> s7 = s5 - s6
		>>> s7.get_linked_bag().vector()
		[]
		"""

		#PYTHONIC WAY
		# lb_new = LinkedBag()
		# lb_new.initialize_from_vector(list(set(self.lb.vector()) & set(set2.get_linked_bag().vector())))
		# return Set(lb_new)

		#Iterate through LinkedBag without using Python shortcuts
		lb = LinkedBag()
		vec = []
		curr = set2.get_linked_bag().get_head()
		while curr != None:
			if self.get_linked_bag().contains(curr.get_data()):
				vec.append(curr.get_data())
			curr = curr.get_next()
		lb.initialize_from_vector(vec)
		return Set(lb)

	def __str__(self):
		s = ""
		for item in self.get_linked_bag().vector():
			s += str(item) + "\n"
		return s

if __name__ == '__main__':
	lb1 = LinkedBag()
	lb1.initialize_from_vector([1,2,'hello',8,5,4,10])
	lb2 = LinkedBag()
	lb2.initialize_from_vector([12,'hello',85,300])
	s1=Set(lb1)
	s2=Set(lb2)
	print("Current s1 is of length %s and has the following items: " % str(s1.getCurrentSize()))
	print(s1)
	print("Current s2 is of length %s and has the following items: " % str(s2.getCurrentSize()))
	print(s2)
	print("Removing 4 and 10 from s1.")
	s1.remove(4)
	s1.remove(10)
	print("Removing 300 from s2.")
	s2.remove(300)
	print("Current s1 is of length %s and has the following items: " % str(s1.getCurrentSize()))
	print(s1)
	print("Current s2 is of length %s and has the following items: " % str(s2.getCurrentSize()))
	print(s2)
	s3 = s1 + s2
	s4 = s1 - s2
	print ("here is s1 union s2: ")
	print(s3)
	print("here is s1 intersect s2: ")
	print(s4)
	print ("Goodbye!")

