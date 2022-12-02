#!/usr/bin/env python3
# @Date       : 2022/4/16 
# @Filename   : 6061.py
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
	def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:	
		l1 = total // cost1
		result = 0
		for i in range(l1+1):
			l2 = (total - i * cost1) // cost2
			result = result + l2 + 1 
		return result
		
		
# -------------------------
		
a = Solution()

#tt = 20
#c1 = 10
#c2 = 5

tt2 = 5
c1 = 10
c2 = 10

print(a.waysToBuyPensPencils(tt2, c1, c2))