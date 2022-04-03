#!/usr/bin/env python3
# @Date       : 2022/3/8 
# @Filename   : 2055.py
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
	def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:		
		n = len(s)
		
		presum = [0] * (n+1)
		lefts = [-1] * n
		rights = [-1] * n
		l = -1
		for i, c in enumerate(s):
			if c == '*':
				presum[i + 1] = presum[i] + 1
			else:
				presum[i + 1] = presum[i]
				l = i
			lefts[i] = l
			
		r = -1
		for i, c in enumerate(s[::-1]):
			if c == '|':
				r = n - 1 -i
			rights[n - 1 - i] = r
		
		result = []
		for l, r in queries:
			if rights[l] >= 0 and lefts[r] >= 0 and rights[l] < lefts[r]:
				result.append(presum[lefts[r]] - presum[rights[l]])
			else:
				result.append(0)
		return result
		
# -------------------------
		
a = Solution()

s1 = "**|**|***|" 
q1 = [[2,5],[5,9]]

s2 = "***|**|*****|**||**|*"
q2 = [[1,17],[4,5],[14,17],[5,11],[15,16]]

print(a.platesBetweenCandles(s2, q2))