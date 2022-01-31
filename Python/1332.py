#!/usr/bin/env python3
# @Date       : 2022/1/22 
# @Filename   : 1332.py
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
	def removePalindromeSub(self, s: str) -> int:
		if s == s[::-1]:
			return 1
		else:
			return 2
		
		
# -------------------------
		
a = Solution()
b = "baabb"

Solution.removePalindromeSub(a, b)