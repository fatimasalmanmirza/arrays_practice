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

	revered = ""
	for i in astring:
		revered = i + revered
	return revered
print(rev_string("abcd"))		
