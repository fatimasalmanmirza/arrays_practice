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
	# counter = 0
	# for i in range(len(nums)-1):
	# 	if nums[i] != nums[i+1]:
	# 		counter +=1

	# return counter
			
	if len(nums) <= 1:
		return len(nums)
	i = 1
	while i < len(nums):
		if nums[i] == nums[i-1]:
			nums.pop(i)
		else:
			i += 1
	return len(nums)				
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))


