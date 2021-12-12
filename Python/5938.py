#!/usr/bin/env python3

class Solution:
	def targetIndices(self, nums: [int], target: int) -> [int]:
		nums.sort()
		if target not in nums:
			return []
		l = nums.index(target)
		result = []
		for i in range(l,len(nums)):
			if nums[i] == target:
				result.append(i)
			else:
				return result
		return result
		
b = [1,2,5,2,3]
c = 2
a = Solution()
print(Solution.targetIndices(a, b, 5))