#!/usr/bin/env python3
# 至少是其他数字两倍的最大数

from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
		
class Solution:
	def dominantIndex(self, nums: List[int]) -> int:
		m1 = m2 = 0
		idx = 0
		for i, num in enumerate(nums):
			if num > m1:
				m2 = m1
				m1 = num
				idx = i
			elif num > m2 :
				m2 = num
		if m1 >= (m2*2):
			return idx
		else:
			return -1
# -------------------------
		
a = Solution()
b = [1]
print(Solution.dominantIndex(a, b))