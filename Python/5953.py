#!/usr/bin/env python3
from typing import List
from itertools import product,combinations,permutations
class Solution:
	def subArrayRanges(self, nums: List[int]) -> int:
		result = 0
		for i in range(len(nums)):
			mmax = mmin = nums[i]
			for j in range(i+1, len(nums)):
				if nums[j]>mmax:
					mmax = nums[j]
				elif nums[j]<mmin:
					mmin = nums[j]
				temp = mmax -mmin
#				print(nums[i], nums[j], "   ",  temp)
				result += temp
#				result.append(max(p)- min(p))
#		print(result)
a = Solution()
b = [4,-2,-3,4,1]
Solution.subArrayRanges(a, b)