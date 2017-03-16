class Stack():
	def __init__(self):
		self.data = []

	def isEmpty(self):
		"""returns True is self.data is empty"""
		return len(self.data) == 0

	def peek(self):
		"""returns last item on stack if non-empty.
			if Stack is empty, return error
		"""
		if self.data:
			return self.data[len(self.data) - 1]
		else:
			raise ValueError

	def push(self, item):
		"""
		pushes item onto Stack.
		return val: True
		"""
		self.data.append(item)
		return True

	def pop(self):
		"""
		pops item off Stack
		return val: True if stak isn't empty, False otherwise
		"""
		if len(self.data) > 0:
			self.data.pop()
			return True
		else:
			return False
