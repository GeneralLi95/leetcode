#!/usr/bin/env python3
# @Date       : 2022/2/27 
# @Filename   : 6009.py
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
	def minSteps(self, s: str, t: str) -> int:
		c1 = Counter(s)
		c2 = Counter(t)
		cnt = 0
		for i, num in c1.items():
			if i in c2:
			
				cnt = cnt + abs(c2[i] - c1[i])
			else:
				cnt += c1[i]
				
		for i, num in c2.items():
			if i not in c1:
				cnt += num
		return cnt
# -------------------------
		
a = Solution()

s1 = "leetcode"
t1 = "coats"

print(a.minSteps(s1, t1))