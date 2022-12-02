#!/usr/bin/env python3
# @Date       : 2022/4/17 
# @Filename   : 6071.py
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
	def minimumRounds(self, tasks: List[int]) -> int:
		tc = Counter(tasks)
		result = 0
		for i in tc.values():
			if i == 1:
				return -1
			else:
				cnt = 0
				temp1 = i % 3
				if temp1 == 0:
					cnt = i // 3
				if temp1 == 2:
					cnt = i // 3 + 1
				if temp1 == 1:
					cnt = i // 3 - 1 + 2
			result += cnt
		return result
				
		
		
		
# -------------------------
		
a = Solution()
t = [2,2,3,3,2,4,4,4,4,4]

print(a.minimumRounds(t))