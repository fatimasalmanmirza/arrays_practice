# def lengthOfLIS(nums):

# 	result = []
# 	current_window = [nums[0]]
# 	for i in range(1,len(nums)):
			
# 		if nums[i] > current_window[-1]:
# 			current_window.append(nums[i])
# 			result.append(current_window)
# 		elif nums[i] <= current_window[-1]:
# 			current_window = [nums[i]]
# 	for i in result:
				
# 		result.append(current_window)
# 		return result


 # print(lengthOfLIS([10,9,2,5,3,7,101,18]))

def remove_duplicates(nums):
	"""remove dupliactes in place"""
		
	if len(nums) <= 1:
		return len(nums)
	i = 1
	while i < len(nums):
		if nums[i] == nums[i-1]:
			nums.pop(i)
		else:
			i += 1
	return nums		
# print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

def contain_duplicates(nums):
	x = set(nums)
	if len(nums) != len(x):
		return True
	return False	
# print(contain_duplicates([1,1,1,3,3,4,3,2,4,2]))

def singleNumber(nums):
	
	count = 0
	nums.sort()
	current = nums[0]
	for i in range(len(nums)):
		if current == nums[i]:
			count += 1
		else:
			if count == 1:
				return current
			current = nums[i]
			count = 1
	if count == 1:
		return current
# print(singleNumber([4,1,2,1,2]))

def intersect(nums1, nums2):
	result = []
	map = {}
	for i in nums1:
		if i not in map:
			map[i] = 1
		else:
			map[i] += 1			
	for j in nums2:
		if j in map and map[j] > 0:
			result.append(j)
			map[j] -= 1
	return result
# print(intersect([1,2,2,1],[2,2]))
# print(intersect([4,9,5],[9,4,9,8,4]))

def intersection(nums1, nums2):
	result = []
	map = {}
	for i in nums1:
		if i in nums2:
			if i not in result:
				result.append(i)
	return result
# print(intersection([1,2,2,1],[2,2])) 

def plusOne(digits):
	num = 0
	for i in digits:
		num = 10 * num + i
	num = num + 1
	print(num)

	num_list = []
	while num > 0:

		a= num //10
		
		r = num % 10
		num_list.append(r)
		num = a
	return num_list[::-1]	
# print(plusOne([4,3,2,1]))

# def moveZeroes(nums):
	
# 	for i in range(len(nums)-1):
# 		if nums[i] == nums[i+1]:
# 			nums[i] == nums[i+1]
# 			nums[i+1] == 0
# 	return nums	
# print(moveZeroes([0,1,0,3,12]))	

def rotate(nums,k):

	if k < len(nums):
		k = k
	else:
		k = k-len(nums)	
	

	nums[:] = nums[-k:] +nums[:-k]
	

	return nums
# print(rotate([1,2,3,4,5,6,7],3))
# print(rotate([1,2],3))
def getRow(board, r):
	return board[r]
def getCol(board, c):
	for i in range(9):
		return(board[i][c])	
def getBox(board, boxid):
	result = []
	row = boxid // 3 * 3
	col = boxid % 3 * 3
	for i in range(3):
		for j in range(3):
			result.append(board[row+i][col+j])
	return result		
def validate(l):
	seen = set()
	for i in l:
		if i == ".":
			continue
		if i in seen:
			return False
		else:
			if int(i) >= 0 and int(i) <= 9:
				seen.add(i)
			else:
				return False
	return True
def isValidSudoku(board):
	for i in range(9):
		rowlist = getRow(board, i)
		collist = getCol(board, i)
		if not validate(rowlist) or not validate(collist):
			return False
	for boxid in range(9):
		if not validate(getBox(board,boxid)):
			return False
	return True


# print(isValidSudoku([
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]))	
# print(isValidSudoku([
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]))


# def isSubsequence(s,t):
# 	x = set(s).intersection(set(t))
# 	if set(s) != x:
# 		return False
# 	j = 0
# 	for i in range(len(t)):
# 		if s[j] == t[i]:
# 			j+=1
# 	if j == len(s):
# 		return True
# 	return False			


# print(isSubsequence("abc", "ahbgdc"))	

def lengthoflongestsubstring(s):
	current_set = set()
	i = 0
	current_start = 0
	strings = []
	while current_start <= len(s)-1:
		current_set.clear()
		i = current_start
		while i < len(s) and s[i] not in current_set:
			current_set.add(s[i])
			i+=1		
		strings.append(s[current_start:i])
		current_start += 1
	counter = 0
	for i in strings:
		if len(i) > counter:
			counter = len(i)
	return counter	
# print(lengthoflongestsubstring(""))	
# print(lengthoflongestsubstring("1"))	
# print(lengthoflongestsubstring("zaki"))	
# print(lengthoflongestsubstring("zakifatimapalwasha"))	
# print(lengthoflongestsubstring("abcabcbb"))	
# print(lengthoflongestsubstring("pwwkew"))

def groupAnagrams(strs):
	result = []
	map_words = {}
	for words in strs:
		x = "".join(sorted(words))
		
		if x not in map_words:
			map_words[x] = [words]
		else:
			map_words[x].append(words)
	for k,v in map_words.items():
		result.append(v)
	return result

# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
def validate_overlap(interval, num):
	if num >= interval[0] and num <= interval[1]:
		return True
	return False
# print(validate_overlap([1,3], 6))

def max_intervalvalue(intervals):
	result = 0
	for i in intervals:
		if i[1] >= result:
			result = i[1]
	return result
# print(max_intervalvalue([[1,3],[2,6],[8,10],[15,18]]))	

def merge(intervals):
	
	x = max_intervalvalue(intervals)
	for i in range(x):
		overlapping = []
		for j in intervals:
			if validate_overlap(j,i):
				overlapping.append(j)
		# print(f"{i}: {overlapping}")
	return overlapping

# print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[4,5]]))
def numUniqueEmails(emails):

	seen = set()
	for email in emails:
		local, domain = email.split("@")
	
		local = local.replace(".","")
		print(local)
		if "+" in local:
			local = local.split("+")
			local = local[0]
			seen.add(local+"@" + domain)
		seen.add(local+"@" + domain)
	return len(seen)		
# print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
# 	"testemail+david@lee.tcode.com"]))
def isValid_parens(s):
	openings = ["(", "[", "{"]
	parens_dict = {"]":"[", ")":"(", "}":"{"}
	stack = []
	if len(s) == 1:
		return False
	for i in s:
		if i in openings:
			stack.append(i)
		else:
			if len(stack) == 0:
				return False
			if parens_dict[i] != stack.pop():
					return False
				
	if len(stack) >= 1:
		return False
				
	return True	
# print(isValid_parens("([)]"))
# print(isValid_parens("{[]}"))
# print(isValid_parens("("))

def subdomain_visits(cpdomains):
	domain_dict = {}
	result = []
	for domain in cpdomains:
		count, domain = domain.split(" ")
		count = int(count)
		d = domain.split(".")
		for k in range(1,len(d)+1):
			dd = ".".join(d[-k:])
			if dd not in domain_dict:
				domain_dict[dd] = count
	
	for k,v in domain_dict.items():
		result.append(str(v) + " " + str(k))
	return result				
# print(subdomain_visits(["900 google.mail.com",
#  "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))						

def reverse_string(s):
	left = 0
	right = len(s) - 1
	while left < right:
		temp = s[left]
		s[left] = s[right]
		s[right] = temp
		left +=1
		right -=1
	return s	

# print(reverse_string(["H","a","n","n","a","h"]))	
 
def move_zeroes(nums):
	for i in nums:
		if i == 0:
			nums.remove(i)
			nums.append(i)
	return nums		
# print(move_zeroes([0,1,0,3,12]))	
def backspace(s):
	result = []
	for i in s:
		if i != "#":
			result.append(i)
		else:
			if len(result) != 0:
				result.pop()
	return result			
# print(backspace("a##c"))
def longest_common_prefix(strs):
	if len(strs) < 1:

		return ""
	shortest_string = min(strs, key = len)
	for index,v in enumerate(shortest_string):
		for i in strs:
			if i[index] != v:
				return shortest_string[:index]
# print(longest_common_prefix(["flower","flow","flight"]))	
def findmedian(nums1, nums2):
	join_list = nums1 + nums2

	join_list.sort()

	
	if len(join_list) % 2 != 0:
		index = len(join_list)//2
		return [join_list[index]]
		
	else:
		index = len(join_list)//2
		y = join_list[index]
		z = join_list[index+1]
		x = y+z
		print(x/2)

# print(findmedian([1, 3],[2]))
# print(findmedian([1, 2],[3, 4]))
def merge(intervals):
	if not intervals:
		return []
	data = []
	for interval in intervals:
		data.append((interval[0], 0))
		data.append((interval[1], 1))
	# print(data)	
	data.sort()

	merged = []
	stack = [data[0]]

	for i in range(1, len(data)):
		d = data[i]
		if d[1] == 0:
			stack.append(d)
		elif d[1] == 1:
			if stack:
				start = stack.pop()
			if len(stack) == 0:				
				merged.append( (start[0], d[0]))
	return merged

# print(merge([[1,3],[2,6],[8,10],[15,18]]))

def split_square_digits(n):
	s = 0
	while n >= 1:
		a = n // 10
		b = n % 10
		n = a
		s += b*b

	print(s)
	return s	

def isHappy(n: int) -> bool:
    seen = set()
    while n > 1:
        seen.add(n)
        n = split_square_digits(n)

        if n in seen:
            return False
    print(seen)        
    return True

print(isHappy(19))

