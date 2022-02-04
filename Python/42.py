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
		ans = 0
		stack = list()
		n = len(height)
		
		for i, h in enumerate(height):
			while stack and h > height[stack[-1]]:
				top = stack.pop()
				if not stack:
					break
				left = stack[-1]
				currWidth = i - left - 1
				currHeight = min(height[left], height[i]) - height[top]
				ans += currWidth * currHeight
			stack.append(i)
			
		return ans 
				

# -------------------------
		
a = Solution()
b = [0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(b))