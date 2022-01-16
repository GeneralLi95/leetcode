#!/usr/bin/env python3

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def totalMoney(self, n: int) -> int:
		result = 0
		for i in range(1,n+1):
			if i % 7 == 0:
				money = i//7 - 1 + 7
			else:
				money = i//7 + i%7
			result += money
			
		return result
		
		
# -------------------------
		
a = Solution()
b = 20
print(Solution.totalMoney(a, b))