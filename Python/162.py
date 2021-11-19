#!/usr/bin/env python3

class Solution:
	def findPeakElement(self, nums: [int]) -> int:
		if len(nums) == 0:
			return -1
		
		left = 0
		right = len(nums)
		while left < right:
			mid = (left + right) // 2
			if nums[mid] < nums[mid+1]:
				left = mid+1
				
			else:
				right = mid
				
	# Post-processing:
	# End Condition: left == right
				
		return left
	
a = Solution()
print(Solution.findPeakElement(a, [1,3,2,1]))