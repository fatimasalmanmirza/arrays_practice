def longestCommonPrefix(strs):
	"""Write a function to find the longest common
	prefix string amongst an array of strings.
	If there is no common prefix, return an empty string"""
	if not strs:
		return ""
	shortest_str = min(strs, key = len)
	# print(len(shortest_str))
	for indx, val in enumerate(shortest_str):
		# print(f"{indx}{val}")
		for i in strs:
			if i[indx] != val:
				return shortest_str[:indx]
	return shortest_str			
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

	
		# if domain_s not in domain_dict:
		# 	domain_dict[domain_s] = count
		# else:
		# 	domain_dict[domain_s] += count	



# print(subdomainVisits(["9001 discuss.leetcode.com"]))		
print(subdomainVisits(["900 google.mail.com", "50 yahoo.com",
	"1 intel.mail.com", "5 wiki.org"]))







