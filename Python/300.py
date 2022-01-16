#!/usr/bin/env python3

# 最长递增子序列
from typing import List
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0
		dp = []
		for i in range(len(nums)):
			dp.append(1)
			for j in range(i):
				if nums[i] > nums[j]:
					dp[i] = max(dp[i], dp[j] + 1)
		return max(dp)
		
		
a = Solution()
b = [10,9,2,5,3,7,101,18]
Solution.lengthOfLIS(a, b)