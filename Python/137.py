#!/usr/bin/env python3
# @Date       : 2022/1/31 
# @Filename   : 137.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
# 哈希表
#class Solution:
#	def singleNumber(self, nums: List[int]) -> int:		
#		c = Counter(nums)
#		for i, j in c.items():
#			if j == 1:
#				return i
		
# -------------------------
# 位运算，计算出每一位的和，然后对3取余
class Solution:
	def singleNumber(self, nums: List[int]) -> int:		
		ans = 0
		for i in range(32):
			total = sum((num>>i) & 1 for num in nums)
			if total % 3:
				if i == 31:
					ans -= (1 << i)
				else:
					ans |= (1<<i)
		return ans
		
		
# --------------------------
a = Solution()