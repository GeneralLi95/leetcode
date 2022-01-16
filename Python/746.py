#!/usr/bin/env python3

# 746 使用最小的花费爬楼梯 
# 动态规划
from typing import List
class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		n = len(cost)
		dp = [0] * (n+1)
		for i in range(2,n+1):
			dp[i] = min(dp[i-1] +cost[i-1], dp[i-2] + cost[i-2])
		return dp[n]
		
		
a = Solution()
b = [1,100,1,1,1,100,1,1,100,1]
Solution.minCostClimbingStairs(a, b)
