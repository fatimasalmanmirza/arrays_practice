import math
import os
import random
import re
import sys


def reverse_string(s):
	result = ""
	for i in s:
		result = i + result
	return result

# Complete the substrCount function below.
def is_palin(x):
	return x == reverse_string(x)

def substrCount(s):
	counter = 0
	for k in range(len(s)):
		for i in range(len(s) - k + 1):
		
			sub = s[i:i+k]
			if len(sub) > 0:
				a = is_palin(sub)
				if a == True:
					
					counter +=1
	return counter

if __name__ == '__main__':
	s = 'abcba' #10
	# s = 'asasd' #7
	# s = 'aaaa'  #10
	result = substrCount(s)
	print(result)


