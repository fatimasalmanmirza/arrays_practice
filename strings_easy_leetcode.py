#add_strings
def string_int(num):
	"""converting string to ascii"""
	num_dict = {"0":0, "1":1, "2": 2,
	"3": 3, "4": 4, "5":5, "6":6, "7": 7,
	"8":8, "9":9}

	result = 0
	current = 0
	while current < len(num):
		if num[current] in num_dict:

			result = num[current]

			current += 1


			
	return result	

# print(string_int("11"))

def convert_str_int(num):
	num_dict = {"0":0, "1":1, "2": 2,
	"3": 3, "4": 4, "5":5, "6":6, "7": 7,
	"8":8, "9":9}
	result = 0
	for i in num:
		result = 10 * result + num_dict[i]
		print(result)
	return result	
# print(convert_str_int("12"))			



def addstring(num1, num2):
	"""add two non negative integers represented
	as strings return the sum"""
	return convert_str_int(num1) + convert_str_int(num2)
# print(addstring("50","12"))

#####################################################
def reverse_string_inplace(astring):
	"""Reverse list in place.
	You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
	for i in range(len(astring)//2):
		astring[i] = astring[-1]
	return astring	
# print(reverse_string_inplace([1, 2, 3, 4, 5])) 
###################################################
def reverse_string(s):
	left = 0
	right = len(s) - 1
	while left < right:
		temp = s[left]
		s[left] = s[right]
		print(s[left])

		s[right] = temp
		left += 1
		right -=1
	return s
# print(reverse_string(["h","e","l","l","o"]))		
####################################################
def split_string(s,k):
	result = []
	i = 0
	while i < len(s):
		result.append(s[i:i+k])
		i += k
	return result

# print(split_string("abcdef", 3))		

def reverse_k_2k_char(s,k):
	result = ""
	for idx, val in enumerate(split_string(s, k)):
		if idx % 2 == 0:
			result += "".join(reversed(val))
		else:
			result += val
	return result
# print(reverse_k_2k_char("abcdefg", 2))
# print(reverse_k_2k_char("abcdefghij", 3))
# print(reverse_k_2k_char("abcd", 4))
####################################################
def split_sub_str(s, k):
	result = []
	i = 0
	while i < len(s):
		result.append(s[i:i+k])
		i += 1
	return result
# print(split_sub_str("abcd", 2))	
def find_anagrams(s, p):
	result = []
	result_index = []
	sort_list = []
	for index, val in enumerate(split_sub_str(s, len(p))):
		
		result.append("".join(sorted(val)))
	for index, val in enumerate(result):
		if val == sorted(p):
			result_index.append(index)
			
	return result_index	
# print(find_anagrams("abcddc", "ab"))
#####################################################
def diStringMatch(S):
	lo = 0
	hi = len(S)
	result = []
	for char in S:
		if char == "I":
			result.append(lo)
			lo += 1
		else:
			result.append(hi)
			hi -= 1
	return result + [lo]
######################################################	 			
def reverse_words(s):
	"""Given a string, you need to reverse the
	order of characters in each word within a 
	sentence while still preserving whitespace
	and initial word order"""
	s_list = s.split()
	new_list = []
	for i in s_list:
		i = i[::-1]

		new_list.append(i)
	return " ".join(new_list)			
# print(reverse_words("Let's take LeetCode contest"))		
####################################################
def list_withbackspace(S):
	result = []
	for i in S:
		if i != "#":
			result.append(i)
		else:
			if len(result) != 0:
				result.pop()
	return result			

def backspaceCompare(S, T):
	"""Given two strings S and T, return if they
	are equal when both are typed into empty text
	editors. # means a backspace character."""
	S_list = list_withbackspace(S)
	T_list = list_withbackspace(T)
	if S_list == T_list:
		return True
	return False			
	

#print(backspaceCompare("ab#c", "ad#c"))
#print(backspaceCompare("a##c", "#a#c"))
##################################################
def rotateString(A, B):
	"""We are given two strings, A and B.A shift
	on A consists of taking string A and moving 
	the leftmost character to the rightmost position.
	For example, if A = 'abcde', then it will be 
	'bcdea' after one shift on A. Return True if and
	only if A can become B after some number of shifts on A."""
	if len(A) == 0 and len(B) == 0:
		return True

	if len(A) == 0 or len(B) == 0:
		return False
	if len(A) != len(B):
		return False	

	A_strings = A+A
	i, j = 0, 0
	while i < len(B):
		if A_strings[i] == B[j]:
			if A_strings[i:i+len(B) ] == B:
				return True	
		i += 1

	return False			
# print(rotateString("abcde", "cdeab"))
# print(rotateString("abcde", "abced"))
# print(rotateString("","a"))
# print(rotateString("",""))
# print(rotateString("aa", "a"))
####################################################
def buddy_strings(A, B):
	"""Given two strings A and B of lowercase letters,
	return true if and only if we can swap two letters
	in A so that the result equals B."""
	if len(A) == 0 or len(B) == 0:
		return False


	i = 0
	list_A = list(A)
	
	while i < len(A)-1:
		list_A[i], list_A[i+1] = list_A[i+1], list_A[i]
		if list_A == list(B):

			return True
		i += 1
	return False		
# print(buddy_strings("ab", "ba")) #true
# print(buddy_strings("ab", "ab")) #False
# print(buddy_strings("aa", "aa")) # true
# print(buddy_strings("","aa")) #False
print(buddy_strings("aaaaaaabc", "aaaaaaacb")) #true









	
	
		