from Stack import Stack

def balanced_paren(expression):
	"""Make sure parenthesis in infix expression are balanced.
	return True if balanced, False otherwise.
	>>> balanced_paren('a(b)c')
	True
	>>> balanced_paren('a')
	True
	>>> balanced_paren('')
	True
	>>> balanced_paren('a(b)c)')
	False
	>>> balanced_paren('a(b')
	False
	>>> balanced_paren('(')
	False
	>>> balanced_paren(')')
	False
	>>> balanced_paren('a(b)c(d))e')
	False
	"""
	stack = Stack()
	for char in expression:
		if char == "(":
			stack.push(char)
		elif char == ")":
			if stack.isEmpty():
				return False
			stack.pop()
	if not stack.isEmpty():
		return False
	return True

def isLowerLetter(char):
	"""Returns True if char is a lower case letter, False otherwise."""
	return ord(char) >= ord('a') and ord(char) <= ord('z')

def value_order(expression):
	"""Error detection for variables that are together (like bb+c) or operators that are together (like b++c).
	returns True if valid, False if errors detected.
	>>> value_order('bb+c')
	False
	>>> value_order('b++c')
	False
	>>> value_order('a(+b)')
	False
	>>> value_order('a+(b)')
	True
	>>> value_order('(a+b)')
	True
	>>> value_order('a+(b-)c')
	False
	>>> value_order('a')
	True
	>>> value_order('')
	True
	>>> value_order('+')
	False
	>>> value_order('(')
	False
	>>> value_order(')')
	False
	>>> value_order('a+')
	False
	"""
	if len(expression) < 1:
		return True
	elif isLowerLetter(expression[0]) and len(expression) == 1:
		return True
	elif len(expression) < 3:
		return False
	else:
		prevOperand, prevOperator = False, True
		i = 0
		loop = True
		while loop:
			if isLowerLetter(expression[i]):
				prevOperand = True
				prevOperator = False
				loop = False
			elif expression[i] == "(":
				while expression[i] == "(":
					i += 1
			else:
				return False
		for index in range(i+1, len(expression)):
			if isLowerLetter(expression[index]):
				if prevOperand:
					return False
				else:
					prevOperand, prevOperator = True, False
			elif expression[index] == "(" and index > 0:
				if prevOperand:
					return False
			elif expression[index] == ")":
				if prevOperator:
					return False
			else:
				if prevOperator:
					return False
				else:
					prevOperand, prevOperator = False, True
		return True

def valid_infix(expression):
	"""Determines whether input infix expression is valid
	assumptions:
	1) variables are single character from a to z (lowercase)
	2) There are no unary minus or plus operators
	3) There are no spaces
	returns True if valid, False otherwise
	>>> valid_infix("a/(b-c)*z")
	True
	>>> valid_infix("a(b)c(d))e")
	False
	>>> valid_infix('a+(b-)c')
	False
	"""
	return balanced_paren(expression) and value_order(expression)

def infix_to_postfix(expression):
	"""Convert valid infix expression to valid postfix expression.
	Return postfix expression or False if invalid infix expression.
	>>> infix_to_postfix("a-(b+c*d)/e")
	'abcd*+e/-'
	>>> infix_to_postfix("a-(c*d)/e")
	'acd*e/-'
	>>> infix_to_postfix("a+b")
	'ab+'
	>>> infix_to_postfix("a+b*c")
	'abc*+'
	>>> infix_to_postfix("a/(b-c)*z")
	'abc-/z*'
	>>> infix_to_postfix("a+(b*c-d)/f")
	'abc*d-f/+'
	"""
	if valid_infix(expression):
		stack = Stack()
		postfix = ""
		operator_rank = {'*': 1, '/': 1, '+': 0, '-': 0}
		for char in expression:
			case = switch_helper(char)
			if case == 'operand':
				postfix += char
			elif case == 'open':
				stack.push(char)
			elif case == 'operator':
				if stack.isEmpty():
					stack.push(char)
				else:
					while stack.isEmpty() != True:
						c = stack.peek()
						if c != "(":
							if operator_rank[c] < operator_rank[char]:
								break
							else:
								stack.pop()
								postfix += c
						else:
							break
					stack.push(char)
			elif case == "close":
				while stack.isEmpty() != True and stack.peek() != "(":
					c = stack.peek()
					postfix += c
					stack.pop()
				stack.pop()
		#clear out remaining operators in stack
		while not stack.isEmpty():
			c = stack.peek()
			postfix += c
			stack.pop()
		return postfix
	else:
		return False

def switch_helper(exp):
	switch = {
		'*': 'operator',
		'/': 'operator',
		'+': 'operator',
		'-': 'operator',
		'(': 'open',
		')': 'close'
	}
	return switch.get(exp, 'operand')

if __name__ == '__main__':
	loop = True
	while loop:
		infix = raw_input("Enter infix expression: ")
		rtn = infix_to_postfix(infix)
		if rtn == False:
			print ("Invalid infix expression.")
		else:
			print ("postfix: %s") % rtn
		cont = raw_input("Would you like to continue? Answer with yes or no: ")
		if cont == 'yes':
			loop = True
		else:
			loop = False
