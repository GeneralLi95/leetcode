#!/usr/bin/env python3

# 爬楼梯 动态规划

class Solution:
	def climbStairs(self, n: int) -> int:
		dp = [1, 1]
		if n == 1:
			return 1
		else:
			for i in range(n-1):
				temp = dp[i] + dp[i+1]
				dp.append(temp)    # 记忆
		return(temp)

a = Solution()
Solution.climbStairs(a, 4)