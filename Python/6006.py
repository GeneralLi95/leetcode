#!/usr/bin/env python3
# @Date       : 2022/2/13 
# @Filename   : 6006.py
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
	def minimumRemoval(self, beans: List[int]) -> int:		
		beans.sort()
		right = sum(beans)
		left = 0
		res = []
		for i, b in enumerate(beans):
			
			right = right - b
			result = left + right - b * (len(beans) - i - 1)

			res.append(result)
			left += b
		return min(res)
# -------------------------
		
a = Solution()
b = [4,1,6,5]

print(a.minimumRemoval(b))