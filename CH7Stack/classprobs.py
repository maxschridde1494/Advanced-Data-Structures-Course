import sys
from Stack import Stack

def factStack(n):
	"""Implement factorial without using recursion. Use Stack ADT"""
	s = Stack()
	for num in range(1, n+1):
		s.push(num)
	rtnVal = 1
	while not s.isEmpty():
		curr = s.peek()
		print (curr)
		rtnVal *= curr
		s.pop()
	return rtnVal

if __name__ == '__main__':
	n = sys.argv[1]
	f = factStack(int(n))
	print ("%s factorial is %s.") % (n, str(f))

