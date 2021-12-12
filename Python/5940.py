#!/usr/bin/env python3
from typing import List
class Solution:
	def minimumDeletions(self, nums: List[int]) -> int:
		n = len(nums)
		if n == 1:
			return 1
		a = nums.index(max(nums))
		b  = nums.index(min(nums))
		
	
		left =  min(a,b)
		right = max(a,b)
		l1 = right + 1
		l2 = n - left
		l3 = left+1 + n-right
		return (min(l1,l2,l3))
		
		
a = Solution()
b = [0,-4,19,1,8,-2,-3,5]
b2 = [2,10,7,5,4,1,8,6]

print(Solution.minimumDeletions(a, b2))