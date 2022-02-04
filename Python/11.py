#!/usr/bin/env python3
# @Date       : 2022/2/4 
# @Filename   : 11.py 盛最多水的容器 
# @Tag        : 贪心，双指针，数组
# @Autor      : LI YAO
# @Difficulty : Medium

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
	def maxArea(self, height: List[int]) -> int:		
		l = 0
		r = len(height) - 1
		contain = 0
		while l < r:
			contain = max(contain, (r-l) * min(height[l], height[r]))
			if height[l] <= height[r]:
				l += 1
			else:
				r -= 1
			
		return contain
		
# -------------------------
		
a = Solution()
b = [1,8,6,2,5,4,8,3,7]

print(a.maxArea(b))