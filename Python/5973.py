#!/usr/bin/env python3
# @Date       : 2022/1/22 
# @Filename   : 5973.py
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
	def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
		
		
		
# -------------------------
		
a = Solution()

g = [[1,2,0,1],[1,3,3,1],[0,2,5,1]]
p = [2,3]
s = [2,3]
b = 2

print(Solution.highestRankedKItems(a, g, p, s, b))