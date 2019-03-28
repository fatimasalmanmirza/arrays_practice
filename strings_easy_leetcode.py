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












	
	
		