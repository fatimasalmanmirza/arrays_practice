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
	reverse_w = []
	result = ""
	reverse_w = s.split()
	for i in s:
		result = i + result
		reverse_w = list(result)
	return "".join(reverse_w[::-1])	
		

	
print(reverse_words("Let's take LeetCode contest"))		












	
	
		