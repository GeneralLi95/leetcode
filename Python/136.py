#!/usr/bin/env python3
# @Date       : 2022/1/31 
# @Filename   : 136.py 只出现一次的数字
# @Tag        : 位运算，数组
# @Autor      : LI YAO
# @Difficulty : Easy

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
# 哈希表 需要额外开空间
#class Solution:
#	def singleNumber(self, nums: List[int]) -> int:
#		c = Counter(nums)
#		for i, j in c.items():
#			if j == 1:
#				return i
		
# -------------------------
class Solution:
	def singleNumber(self, nums: List[int]) -> int:		
		result = 0
		for i in nums:
			result ^= i
		return result
# ------------------------
a = Solution()
a.singleNumber([2,2,1])