
def even_odd(A):
	next_even, next_odd = 0, len(A) - 1
	while next_even < next_odd:
		if A[next_even] % 2 == 0:
			next_even += 1
		else:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd -= 1
	return A	
print(even_odd([2,3,5,11,6,8]))