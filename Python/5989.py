#!/usr/bin/env python3
# @Date       : 2022/1/23 
# @Filename   : 5989.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

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
class Solution:
	def countElements(self, nums: List[int]) -> int:
		
		m1 = min(nums)
		m2 = max(nums)
		c1 = nums.count(m1)
		c2 = nums.count(m2)
		
		count = len(nums) - c1 -c2
		if count < 0 :
			return 0
		return count
		
		
		
		
# -------------------------
		
a = Solution()
b = [-3,-3,3,3,4,90]
c= [0]

print(Solution.countElements(a, c))