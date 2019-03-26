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

print(string_int("11"))

def convert_str_int(num):
	num_dict = {"0":0, "1":1, "2": 2,
	"3": 3, "4": 4, "5":5, "6":6, "7": 7,
	"8":8, "9":9}
	result = 0
	for i in num:
		result = 10 * result + num_dict[i]
	return result	
print(convert_str_int("12"))			



def addstring(num1, num2):
	"""add two non negative integers represented
	as strings return the sum"""
	return convert_str_int(num1) + convert_str_int(num2)
print(addstring("50","12"))

#####################################################
# def reverse_string(s):
# 	for i in range(len(s)):

	
	
		