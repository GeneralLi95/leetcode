#!/usr/bin/env python3
# @Date       : 2022/4/16 
# @Filename   : 6060.py
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
class Solution:
	def findClosestNumber(self, nums: List[int]) -> int:
		min_result = nums[0]
		for i in nums:
			if abs(i - 0) < abs(min_result - 0):
				min_result = i
			elif abs(i - 0) == abs(min_result - 0):
				min_result = max(min_result, i)
		return min_result
		
		
# -------------------------
		
a = Solution()