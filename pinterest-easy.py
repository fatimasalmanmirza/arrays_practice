def longestCommonPrefix(strs):
	"""Write a function to find the longest common
	prefix string amongst an array of strings.
	If there is no common prefix, return an empty string"""
	if not strs:
		return ""
	min_l = min(len(S) for S in strs)
	
	for i in range(min_l):
		s = set()
		for x in strs:
			s.add(x[i])
			if len(s) > 1:
				min_l = i
				break
	return strs[0][:min_l]		
# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))		
########################################################
def subdomainVisits(cpdomains):
	"""We are given a list cpdomains of count-paired
	domains. We would like a list of count-paired domains,
	(in the same format as the input, and in any order),
	that explicitly counts the number of visits to each 
	subdomain."""
	from collections import Counter
	domain_dict = Counter()
	result = []
	for domain in cpdomains:
		count, domain = domain.split(" ")
		count = int(count)
		d = domain.split(".")
		for k in range(1, len(d)+1):
			domain_dict[".".join(d[-k:])]+=count
	for keys, values in domain_dict.items():
		result.append(str(values) + " " +str(keys))
	return result			 
# print(subdomainVisits(["9001 discuss.leetcode.com"]))		
# print(subdomainVisits(["900 google.mail.com", "50 yahoo.com",
# 	"1 intel.mail.com", "5 wiki.org"]))
#########################################################
def split_square_digits(n):
	s = 0
	while n >= 1:
		a = n // 10
		b = n % 10
		n = a
		s += b*b
	return s	

def ishappy(n):
# 	"""Write an algorithm to determine if a number is "happy"."""
	seen = set()
	while n > 1:
		seen.add(n)
		n = split_square_digits(n)		
		if n in seen:
			return False
	return True
#########################################################	
def longest_word(words):

	words.sort()
	words_set = set([""])
	result =  ''
	for word in words:
		if word[:-1] in words_set:
			words_set.add(word)
			if len(word) > len(result):
				result = word
	return result
print(longest_word(["w","wo","wor","worl", "world"]))
print(longest_word(["a", "banana", "app", "appl", "ap", "apply", "apple"]))






