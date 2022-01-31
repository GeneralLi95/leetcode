#!/usr/bin/env python3
# @Date       : 2022/1/25 
# @Filename   : 1688.py
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
	def numberOfMatches(self, n: int) -> int:
		if n == 1:
			return 0
		result = 0
		while n != 1:
			if n % 2 == 1:
				result += n // 2
				n = n // 2 + 1
				
			else:
				result += n // 2
				n = n // 2

				
		return result 
		
		
		
		
# -------------------------
		
a = Solution()
b = 14
print(Solution.numberOfMatches(a, b))