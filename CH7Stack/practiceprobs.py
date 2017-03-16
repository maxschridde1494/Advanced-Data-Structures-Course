from Stack import Stack

def balancedBraces(string):
	"""Return true if string is balanced with braces, false otherwise
	>>> balancedBraces("{a{b}c}")
	True
	>>> balancedBraces("a")
	True
	>>> balancedBraces("")
	True
	>>> balancedBraces("{a{b}c")
	False
	>>> balancedBraces("{ab}c}")
	False
	>>> balancedBraces("{")
	False
	>>> balancedBraces("}")
	False
	>>> balancedBraces("}a{")
	False
	"""
	s = Stack()
	i = 0 
	while i < len(string):
		c = string[i]
		if c == "{":
			s.push(c)
		elif c == "}":
			if s.isEmpty():
				return False
			else:
				s.pop()
		i += 1
	return s.isEmpty()


