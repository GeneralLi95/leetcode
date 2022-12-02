#!/usr/bin/env python3
# @Date       : 2022/4/16 
# @Filename   : lccup2022spring-1.py
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
	def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
		for op in operations:
			give = gem[op[0]] // 2
			gem[op[0]] -= give
			gem[op[1]] += give
		return max(gem) - min(gem)
		
		
# -------------------------
		
a = Solution()
g = [3,1,2]
op = [[0,2],[2,1],[2,0]]
g1 = [100,0,50,100]
op1 = [[0,2],[0,1],[3,0],[3,0]]
print(a.giveGem(g1, op1))