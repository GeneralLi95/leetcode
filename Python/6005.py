#!/usr/bin/env python3
# @Date       : 2022/2/13 
# @Filename   : 6005.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter, OrderedDict
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def minimumOperations(self, nums: List[int]) -> int:
		n = len(nums)
		g1 = nums[::2]
		g2 = nums[1::2]
		c1 = Counter(g1).most_common()
		c2 = Counter(g2).most_common()
		
		cand1, cand1Count = c1[0] if c1 else (0, 0)
		cand2, cand2Count = c1[1] if len(c1) > 1 else (0, 0)
		cand3, cand3Count = c2[0] if c2 else (0, 0)
		cand4, cand4Count = c2[1] if len(c2) > 1 else (0, 0)
		if cand1 != cand3:
			return n - cand1Count - cand3Count
		else:
			return min(n - cand2Count - cand3Count, n - cand1Count - cand4Count)

# -------------------------
		
a = Solution()
b1 = [3,1,3,2,4,3]
b2 = [1,2,2,2,2]

print(a.minimumOperations(b2))