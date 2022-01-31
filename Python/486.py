#!/usr/bin/env python3
# @Date       : 2022/1/20 
# @Filename   : 486.py 预测赢家
# @Tag        : 动态规划、递归
# @Autor      : LI YAO
# @Difficulty : Medium 实际是Hard 

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
# 动态规划
class Solution:
	def PredictTheWinner(self, nums: List[int]) -> bool:
		n = len(nums)
		dp = [[0] * n for _ in range(n)]
		for i, num in enumerate(nums):
			dp[i][i] = num
		for i in range(n-2, -1, -1):
			for j in range(i+1, n):
				dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
		return dp[0][n-1] >= 0
# -------------------------
		
a = Solution()
b = [1,5,2,4,6]
Solution.PredictTheWinner(a, b)