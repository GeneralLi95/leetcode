#!/usr/bin/env python3
# @Date       : 2022/2/26 
# @Filename   : 2016.py 增量元素之间的最大差值
# @Tag        : 数组
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
class Solution:
	def maximumDifference(self, nums: List[int]) -> int:
		result = 0
		for i in range(len(nums) - 1):
			for j in range(i+1, len(nums)):
				result = max(result, nums[j] - nums[i])
				
		if result == 0:
			result = -1
		return result
		
# -------------------------
		
a = Solution()
b = [1,5,2,10]

print(a.maximumDifference(b))