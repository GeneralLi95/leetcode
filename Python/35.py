#!/usr/bin/env python3

class Solution:
	def searchInsert(self, nums: [int], target: int) -> int:
		left = 0
		right = len(nums) - 1
		while left <= right:
			mid = (left + right)//2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				right = mid-1
			else:
				left = mid+1
			if left>=right and nums[right] < target:
				return right+1
			if left>=right and nums[right] > target:
				return left
			
a = Solution()
print(Solution.searchInsert(a, [1], 0))