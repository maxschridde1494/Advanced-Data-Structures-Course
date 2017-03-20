from radixsort import makeString, generate_x_strings, radix_sort

def quick_sort(arr):
	"""Quicksort implemented where pivot is median of first, middle and last element of arr"""
	if len(arr) < 2:
		return arr
	else:
		#choose pivot as first element if less than 3 elements in arr
		if len(arr) < 3:
			p = arr[0]
			temp_arr = arr[1:]
		else:
			piv_choices = [arr[0], arr[len(arr)/2], arr[len(arr)-1]]
			piv_choices.sort()
			p = piv_choices[1]
			if p == arr[0]:
				temp_arr = arr[1:]
			elif p == arr[len(arr)/2]:
				temp_arr = arr[:len(arr)/2] + arr[len(arr)/2 + 1:]
			else:
				temp_arr = arr[:len(arr)-1]
		l,r = [],[]
		for item in temp_arr:
			if item <= p:
				l.append(item)
			else:
				r.append(item)
		l = quick_sort(l)
		r = quick_sort(r)
		return l + [p] + r

if __name__ == '__main__':
	str_arr = generate_x_strings(10000)
	str_arr_cpy = str_arr[:]
	str_arr_cpy2 = str_arr_cpy[:]
	sorted_str_arr = radix_sort(str_arr, 15)
	str_arr_cpy.sort()
	str_arr_cpy2 = quick_sort(str_arr_cpy2)
	print("last 10 of radix")
	print(sorted_str_arr[len(sorted_str_arr) - 11:])
	print("last 10 of sorted")
	print(str_arr_cpy[len(str_arr_cpy) - 11:])
	print("last 10 of quicksort")
	print(str_arr_cpy2[len(str_arr_cpy2) - 11:])
