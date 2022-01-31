#!/usr/bin/env python3
# @Date       : 2022/1/22 
# @Filename   : 5971.py
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
	def minimumCost(self, cost: List[int]) -> int:
		cost.sort(reverse=True)
		c = deque(cost)
		sum = 0
		temp = 0
		while c:
			if temp == 2:
				temp = 0
				c.popleft()
				continue
			sum += c.popleft()
			temp += 1
		return sum
		
		
# -------------------------
		
a = Solution()
b = [5,5]
print(Solution.minimumCost(a, b))