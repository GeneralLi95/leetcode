#!/usr/bin/env python3
# @Date       : 2022/2/11 
# @Filename   : 1984.py
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
	def minimumDifference(self, nums: List[int], k: int) -> int:
		a = Counter()
		
		
# -------------------------
		
a = Solution()