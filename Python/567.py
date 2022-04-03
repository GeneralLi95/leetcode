#!/usr/bin/env python3
# @Date       : 2022/2/12 
# @Filename   : 567.py 字符串的排雷
# @Tag        : 滑动窗口
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
	def checkInclusion(self, s1: str, s2: str) -> bool:		
		k = len(s1)
		c1 = Counter(s1)
		for i in range(len(s2) - k + 1):
			c2 = Counter(s2[i:i+k])
			if c1 == c2 :
				return True
		return False
		
# -------------------------
		
a = Solution()
b1 = "hello"
b2 = "ooolleoooleh"

b3 = "ab"
b4 = "ba"
print(a.checkInclusion(b1, b2))