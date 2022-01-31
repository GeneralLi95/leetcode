#!/usr/bin/env python3
# @Date       : 2022/1/20 
# @Filename   : 2029.py
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
	def stoneGameIX(self, stones: List[int]) -> bool:
		cnt0 = cnt1 = cnt2 = 0
		for val in stones:
			if val % 3 == 0:
				cnt0 += 1
			elif val % 3 == 1:
				cnt1 += 1
			else:
				cnt2 += 1
		if cnt0 % 2 == 0:
			return cnt1 >= 1 and cnt2 >= 1
		return cnt1- cnt2 > 2 or cnt2 - cnt1 > 2
		
		
# -------------------------
		
a = Solution()
b = [5,1,2,4,3]