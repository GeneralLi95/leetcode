#!/usr/bin/env python3
from typing import List
class Solution:
	def getAverages(self, nums: List[int], k: int) -> List[int]:
		if k == 0:
			return nums
		
		n = len(nums)
		
		result = [-1 for i in range(n)]
		for i, num in enumerate(nums):
			if i < k or (n-i-1)<k:
				continue
			if i == k:
				sum_0 = sum(nums[0:k+k+1]) 
				print(sum_0)
				result[i] = sum_0//(k*2+1)
			else:
				sum_0 = sum_0 - nums[i - k - 1] + nums[i+k]
				result[i] = sum_0//(k*2+1)
				print(sum_0)
		return result
		
a = Solution()
b = [7,4,3,9,1,8,5,2,6]
c = 3

print(Solution.getAverages(a, b, c))