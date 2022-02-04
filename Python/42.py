#!/usr/bin/env python3
# @Date       : 2022/2/4 
# @Filename   : 42.py 接雨水
# @Tag        : 栈，数组，双指针，动态规划，单调栈
# @Autor      : LI YAO
# @Difficulty : Hard

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
	def trap(self, height: List[int]) -> int:
		n = len(height)
		for i in range(n):
			if height[i] == 0:
				continue
			
			l.apppend(i)
			
			if height[i] >= height[l]
# -------------------------
		
a = Solution()
b = [0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(b))