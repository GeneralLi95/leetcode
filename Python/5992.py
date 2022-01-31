#!/usr/bin/env python3
# @Date       : 2022/1/23 
# @Filename   : 5992.py
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
	def maximumGood(self, statements: List[List[int]]) -> int:		
		count = 0
		
		
# -------------------------
		
a = Solution()
b = [[2,1,2],[1,2,2],[2,0,2]]
b2 = [[2,0,2,2,0],[2,2,2,1,2],[2,2,2,1,2],[1,2,0,2,2],[1,0,2,1,2]]  # 2

print(Solution.maximumGood(a, b))