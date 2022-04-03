#!/usr/bin/env python3
# @Date       : 2022/3/9 
# @Filename   : 798.py
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
	def bestRotation(self, nums: List[int]) -> int:		
		n = len(nums)
		count = [0] * n
		for i in range(n):
			nl = nums[i:n] + nums[0:i]
			score = 0
			for j, val in enumerate(nl):
				if val <= j:
					score += 1
			count[i] = score
		return count.index(max(count))
		
# -------------------------
		
a = Solution()

n = [2,3,1,4,0]
print(a.bestRotation(n))