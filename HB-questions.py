#Hackbright questions
#Given a string, return a new string that is the original #string, reversed. Do this with recursion, not a for loop.

def rev_string(astring):
	"""Return reverse of string using recursion.
	You may NOT use the reversed() function!
	"""
	if len(astring) < 2:
		return astring
	return astring[-1] + rev_string(astring[0:-1])	
print(rev_string("abcdefg"))
print(rev_string(""))
##########################################################
def rev_string(astring):
	"""without recursion"""
	revered = ""
	for i in astring:
		revered = i + revered
	return revered
print(rev_string("abcd"))
########################################################

def dec2bin(num):
	"""decimal to binary"""
	string = ""
	if num == 0:
		return num
	while num != 0:

		remainder = num%2
		string = str(remainder)+ string
		num = num//2	
	return string
print(dec2bin(6))
#########################################################
def is_anagram_of_palindrome(word):

	counter = 0
	result = {}
	for i in word:
		if i in result:
			result[i] += 1
		else:
			result[i] = 1	
	orphan = []
	if len(word)%2 == 0:
		for value in result.values():
			if value%2 != 0:
				return False
	else:
		for value in result.values():
			if value%2 != 0:
				orphan.append(value)
	if len(orphan) > 1:
		return False
	else:
		return True							
# print(is_anagram_of_palindrome("ab")) #false	
# print(is_anagram_of_palindrome("arceaceb")) #False
# print(is_anagram_of_palindrome("a")) #True
# print(is_anagram_of_palindrome("arceace"))	#True
# print(is_anagram_of_palindrome("")) #True

########################################################
def add_to_zero(nums):
	"""Given list of ints, return True if any to sums to 0."""
	set_nums = set(nums)
	for num in nums:
		if -num in set_nums:
			return True
	return False	
# print(add_to_zero([1, 2, 3])) # False		
# print(add_to_zero([1])) #False
# print(add_to_zero([1, 2, 3, -2])) #True

##########################################################









