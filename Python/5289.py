#!/usr/bin/env python3
# @Date       : 2022/6/12 
# @Filename   : 5289.py
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
	def distributeCookies(self, cookies: List[int], k: int) -> int:	
		distributed = [0] * k
		for i in sorted(cookies, reverse=True):
			print(i)
			min_id = distributed.index(min(distributed))
			distributed[min_id] += i
		print(distributed)
		return max(distributed)
			
		
# -------------------------
		
a = Solution()
cookies = [6,1,3,2,2,4,1,2]
k = 3

c2 = [8,15,10,20, 8]
k2 = 2
print(a.distributeCookies(c2, k2))