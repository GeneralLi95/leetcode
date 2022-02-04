#!/usr/bin/env python3
# @Date       : 2022/2/4 
# @Filename   : 1725.py
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
	def countGoodRectangles(self, rectangles: List[List[int]]) -> int:	
		count = 0
		mt = 0
		for i in rectangles:
			temp  = min(i)
			if temp > mt:
				mt = temp
				count = 1
			elif temp == mt:
				count += 1
		return count
				
		
		
# -------------------------
		
a = Solution()
b = [[2,3],[3,7],[4,3],[3,7]]
print(a.countGoodRectangles(b))