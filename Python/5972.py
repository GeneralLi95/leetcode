#!/usr/bin/env python3
# @Date       : 2022/1/22 
# @Filename   : 5972.py
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
	def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
		r_i = list(range(lower,upper+1))
		temp = 0
		result = [0]
		for i in range(len(differences)):
			result.append(result[-1]+differences[i])
		sum = upper - lower - max(result) + min(result) + 1
		if sum <= 0:
			return 0
		return sum
		
		
# -------------------------
		
a = Solution()
b = [3,-4,5,1,-2]
l = -4
u = 5

print(Solution.numberOfArrays(a, b, l, u))