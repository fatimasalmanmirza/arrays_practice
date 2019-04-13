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


print(isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))	
print(isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))


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
























