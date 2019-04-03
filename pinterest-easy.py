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
print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))		
########################################################

