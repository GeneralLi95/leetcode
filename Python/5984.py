#!/usr/bin/env python3
# @Date       : 2022/2/5 
# @Filename   : 5984.py
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
	def minimumSum(self, num: int) -> int:		
		res = list(str(num))
		res.sort()
		print(res)
		return int(res[0]) * 10 + int(res[1]) * 10 + int(res[2]) + int(res[3])
		
# -------------------------
		
a = Solution()
b = 4009

print(a.minimumSum(b))