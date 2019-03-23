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
print(num_unique_emails(["f.atima@live.com","fatima+sal@live.com",
	"fati+ma.s@li+ve.com", "fatima2@live.com"]))

