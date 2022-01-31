#!/usr/bin/env python3
# @Date       : 2022/1/17 
# @Filename   : 1220.py 统计元音字母序列的数目
# @Tag        : 动态规划
# @Autor      : LI YAO
# @Difficulty : Hard

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


MOD = int(1e9)+7
# -------------------------
class Solution:
	def countVowelPermutation(self, n: int) -> int:
		result = [[1]*5] + [[0]*5 for _ in range(n-1)]
		for i in range(1, n):
			result[i][0] = (result[i-1][1] + result[i-1][2] + result[i-1][4])%MOD   	            #a
			result[i][1] = (result[i-1][0] + result[i-1][2])%MOD               					#e
			result[i][2] = (result[i-1][1] + result[i-1][3])%MOD              					#i
			result[i][3] = result[i-1][2]  								 					#o	
			result[i][4] = (result[i-1][2] + result[i-1][3])%MOD 				 					#u
		return (sum(result[n-1]))%MOD
		
		
# -------------------------
		
a = Solution()
print(Solution.countVowelPermutation(a, 5))