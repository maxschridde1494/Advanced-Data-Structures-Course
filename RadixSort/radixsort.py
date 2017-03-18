from random import random
from queuell import QueueLinkedList

def makeString():
	"""
	Generate and return a random string of all printable characters from ASCII 32-126
	i.e. from chr(32) - chr(126)
	Strings are at most length 15 and at least 1 char long
	"""
	s = ""
	length = random() * 15
	if length < 1:
		length = 1
	for i in range(round(length)):
		char = chr(round((random() * (126 - 32))) + 32)
		#don't allow first character to be a space
		if i == 0 and char == " ":
			while char == " ":
				char = chr(round((random() * (126 - 32))) + 32)
		s += char
	return s

def generate_x_strings(x):
	arr = []
	for _ in range(x):
		arr.append(makeString())
	return arr

def generate_x_queues(x):
	arr =[]
	for _ in range(x):
		arr.append(QueueLinkedList())
	return arr

def radix_sort(str_arr, MAX_LENGTH):
	#buckets go from 0 to 126-32, 0 is the " " bucket
	bins = generate_x_queues(95)
	for j in range(MAX_LENGTH):
		#put strings into correct queue / bin
		for string in str_arr:
			k = MAX_LENGTH - (MAX_LENGTH + j - len(string)) - 1
			if k < 0:
				#categorize into the space bin
				bucket_index = 0
			else:
				#categorize into bin of string[k]
				bucket_index = ord(string[k]) - 32
			bins[bucket_index].enque(string)
		str_arr = []
		#place all strs back into array starting at bucket 0 --> for " " char
		for b in bins:
			while not b.is_empty():
				str_arr.append(b.peek().get_data())
				b.deque()
	return str_arr

if __name__ == '__main__':
	# str_arr = generate_x_strings(10000)
	# sorted_str_arr = radix_sort(str_arr, 15)
	# print(sorted_str_arr[:10])
	# print(sorted_str_arr[-10:])
	str_arr = generate_x_strings(50)
	sorted_str_arr = radix_sort(str_arr, 15)
	for s in sorted_str_arr:
		print(s + "\n")
