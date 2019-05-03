def get_subtrings(s):
	current_start = 0
	unique_strings = []
	while current_start <= len(s) - 1:
		i = 0
		while i < len(s):
			i += 1
			sub = s[current_start:i]
			if sub:
				unique_strings.append(sub)
		current_start += 1
	return unique_strings
def longest_palindrome(s):
	if len(s)<= 1:
		return s
	if len(set(s)) = 1:
		return s
	pal_subs= []
	subs = get_subtrings(s)
	for i in subs:
		if i[::-1] == i:
			pal_subs.append(i)
	return max(pal_subs, key=len)		

print(longest_palindrome("babad"))
print(longest_palindrome("bab"))			