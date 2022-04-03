#!/usr/bin/env python3
# @Date       : 2022/2/20 
# @Filename   : tt.py
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
	def countEven(self, n) ->int:
		cnt = 0
		for i in range(1,n+1):
			if (i % 10 + i // 10 % 10 + i // 100 % 10 + i // 1000) % 2 == 0:
				cnt += 1
				
		return cnt
# -------------------------
		
a = Solution()
b = 997
print(a.countEven(b))