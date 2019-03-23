# Implement function ToLowerCase() that has 
#a string parameter str, and returns the same string in lowercase.

def to_lower_Case(s):
	lower_s = ""
	for i in s:
		lower_s += i.lower()
	return lower_s	
# print(to_lower_Case("HeTToP-HJ"))

#local name, domain name separated by @
def num_unique_emails(emails):
		
	new_l = []
	for i in emails:
		c = i.split("@")[0]
		d_name = "@" + i.split("@")[1]

		c = c.replace('.','')
		if "+" in c:
			d = c.split("+")[0]
			
			if d+d_name not in new_l:
				new_l.append(d+d_name )
		else:
			if c+d_name not in new_l:
				new_l.append(c+d_name)
	return len(new_l)
# print(num_unique_emails(["f.atima@live.com","fatima+sal@live.com",
# 	"fati+ma.s@li+ve.com", "fatima2@live.com"]))


###########################################################
def asci_to_index(s):
	
	index = ord(s) - ord('a')
	return index

def word_to_morse(word):
    morse_code = [".-","-...","-.-.","-..",".",
        "..-.","--.","....","..",".---","-.-",".-..","--",
        "-.","---",".--.","--.-",".-.","...","-","..-","...-",
        ".--","-..-","-.--","--.."]
    translation = ""
    for i in word:
        i_index = asci_to_index(i)
        translation += morse_code[i_index]
    return translation

def unique_morse_code_words(words):  
	if len(words) < 2:
	 	return len(words)

	uniques =[]
	for word in words:
		morse = word_to_morse(word)
		uniques.append(morse)	
	return len(set(uniques))
# print(unique_morse_code_words([]))

###########################################################
#In a array A of size 2N, 
#there are N+1 unique elements, 
#and exactly one of these elements is repeated N times.
#Return the element repeated N times.
def repeat_elements(elements):
	# repeats = []
	# for i in range(len(elements)-2):
	# 	if elements[i] == elements[i+2]:
	# 		repeats.append(elements[i])
		
	dict_el = {}
	for i in elements:
		if i in dict_el:
			dict_el[i] += 1
		else:
			dict_el[i] = 1

	for k,value in dict_el.items():
		if value > 1:
			return k
print(repeat_elements([2,1,2,5,3,2]))
############################################################

#Given an array of integers
# A sorted in non-decreasing order, 
#return an array of the squares of each number,
# also in sorted non-decreasing order.

def sortedsq(nums):
	result = []
	for i in nums:
		result.append(i**2)
	sorted_list = sorted(result)	

	return sorted_list
		
print(sortedsq([-7,-3,2,3,11]))

###########################################################

#Given an array A of non-negative integers, 
#return an array consisting of all the even elements of A,
#followed by all the odd elements of A.
#You may return any answer array that satisfies this condition.
def sort_array_evenodd(nums):
 	even = []
 	odd = []
 	for i in nums:
 		if i%2 == 0:
 			even.append(i)
 		else:
 			odd.append(i)	

 	
 	return even + odd
print(sort_array_evenodd([3,1,2,4])) 	

