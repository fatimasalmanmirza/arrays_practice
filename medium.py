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
print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))	




