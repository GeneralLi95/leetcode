#!/usr/bin/env python3
# @Date       : 2022/1/29 
# @Filename   : 1765.py
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
	def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:		
		m = len(isWater)
		n = len(isWater[0])
		x, y = min(m,n), max(m,n)
		water = sum(sum(a) for a in isWater)
		land = m*n - water
		
		x1 = water // x
		
		
		return y - x1
		
		
		
# -------------------------
		
a = Solution()
b = [[0,0,1],[1,0,0],[0,0,0]]


print(Solution.highestPeak(a, b))